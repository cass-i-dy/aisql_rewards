import json
from openai import OpenAI
import os
from db_bot import connect_to_sql, create_database, insert_data
import mysql.connector

def read_file(file):
	with open(file, 'r') as file:
		sql = file.read()
		return sql

def runSql(query, cursor):
	cursor.execute(query)
	result = cursor.fetchall()
	return result
def get_api_key():
	with open("config.json", 'r') as file:
		config = json.load(file)
		return config['openaiKey']

def getChatGptResponse(content):
	with open("config.json", 'r') as file:
		config = json.load(file)

	openAiClient = OpenAI(
		api_key=config["openaiKey"],
		organization=config["orgID"]
	)

	# models = openAiClient.models.list()
	# for model in models.data:
	# 	print(model.id)

	stream = openAiClient.chat.completions.create(
		model="gpt-4o-mini",
		messages=[{"role": "user", "content": content}],
		stream=True,
	)

	responseList = []
	for chunk in stream:
		if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content is not None:
			responseList.append(chunk.choices[0].delta.content)
	result = "".join([str(item) for item in responseList if item is not None])
	return result

def sanitizeForJustSql(value):
	gptStartSqlMarker = "```sql"
	gptEndSqlMarker = "```"
	if gptStartSqlMarker in value:
		value = value.split(gptStartSqlMarker)[1]
	if gptEndSqlMarker in value:
		value = value.split(gptEndSqlMarker)[0]
	return value

def ask_question(cursor, strategies, questions):
	strategyResults = []
	for strat in strategies:
		responses = {"strategy" : strat, "prompt_prefix" : strategies[strat]}
		questionResults = []
		for question in questions:
			print(question)
			error = "None"
			sqlSyntaxResponse = None
			queryRawResponse = None
			friendlyResponse = None
			try:
				sqlSyntaxResponse = getChatGptResponse(strategies[strat] + " " + question)
				sqlSyntaxResponse = sanitizeForJustSql(sqlSyntaxResponse)
				print(sqlSyntaxResponse)
				queryRawResponse = str(runSql(sqlSyntaxResponse, cursor))
				print(queryRawResponse)
				friendlyResultsPrompt = "I asked a question \"" + question + "\" and the response was \"" + queryRawResponse + "\" Please, just give a concise response in a more friendly way? Please do not give any other suggestions or chatter."
				friendlyResponse = getChatGptResponse(friendlyResultsPrompt)
				print(friendlyResponse)
			except Exception as err:
				error = str(err)
				print(err)
			questionResults.append({
				"question" : question,
				"sql" : sqlSyntaxResponse,
				"queryRawResponse": queryRawResponse,
				"friendlyResponse" : friendlyResponse,
				"error": error
			})

		responses["questionResults"] = questionResults
		strategyResults.append(responses)
	with open("output.json", "w") as outFile:
		json.dump(strategyResults, outFile, indent = 2)


def main():
	cursor, connection = connect_to_sql()
	create_database(cursor)
	insert_data(cursor, connection)

	commonSqlOnlyRequest = " Give me a mysql select statement that answers the question. Only respond with mysql syntax. If there is an error do not explain it."
	set_up_sql = read_file("setup.sql")
	data_sql = read_file("setupData.sql")
	strategies = {
		"zero_shot": set_up_sql + commonSqlOnlyRequest,
		"single_domain_double_shot": (set_up_sql +
									  " Who doesn't have a way for us to text them? " +
									  " \nSELECT p.person_id, p.name\nFROM person p\nLEFT JOIN phone ph ON p.person_id = ph.person_id AND ph.can_recieve_sms = 1\nWHERE ph.phone_id IS NULL;\n " +
									  commonSqlOnlyRequest)
	}

	questions = [
		"How many customers have ordered?",
		"What is the max rewards someone has?",
		"Who doesn't have an email?",
		"Who all opted out of receiving email updates?",
		"Who has made the most orders?",
		"Who has the same first name as someone else?",
		"Who didn't order anything?",
		"Is everyone ordering food?",
		"What is the most ordered food item?",
		"What is everyone's favorite food?"
	]

	ask_question(cursor, strategies, questions)

	cursor.close()
	connection.close()


if __name__ == '__main__':
	main()


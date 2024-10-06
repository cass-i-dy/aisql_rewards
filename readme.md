# Restaurant Rewards

My project models data that a online rewards app could have in keeping track of customer orders and rewards. Includes contact information, login information, and order information for a person.


<img src="schema.png">

## Query I thought it did well on

Question: What is the most ordered food item?

**GPT SQL RESPONSE**:
```sql
SELECT food_name,
COUNT(*) AS order_count
FROM orders o
JOIN food_reward f ON o.food_id = f.food_id
GROUP BY food_name
ORDER BY order_count DESC
LIMIT 1;,
```

SQL Result is ('Chicken Nuggets', 4)

**Friendly response**: The most ordered food item is Chicken Nuggets!

## Question that it tripped up on

It did find the person who made the most orders and the number, however it didn't specify the name of the person and when reporting the result got the person ID and number of orders confused. 

Question: Who has made the most orders?

**GPT SQL Response**:
```sql
SELECT person_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY person_id
ORDER BY total_orders DESC
LIMIT 1;
```

SQL Result the person ID, and number of orders: [(6, 3)]

**Friendly response** "The person with the most orders has made 6 orders."

The major issue is that it confused the person ID with the number of orders they made. It also didn't return the name of person with the most orders, even though I asked who. Which I think would imply the need for a name since we don't reffer to people by numbers. If I had specified I wanted the name it probably could have a result that was more user friendly.

## Multi-Shot
I attempted the question it struggled to answer, however it still didn't add the "name" attribute and it changed some of the formatting of the answers to different questions. 

**Question (multi-shot)**: Who has made the most orders?

I used the provided the same query that it outputted in the question it struggled with.

SQL Result is numver of orders and person ID: [(6, 3)]

**Friendly response**: The person with the most orders made 6 in total!

Using the multi-shot, it made the same mistakes. In fact looking at the other results it messed with the other questions answers as well. It still is getting the personID and number of orders confused. Some of the questions it pretty much just guessed an answer or responded in an unnecessary way. 

## Conclusion
I found that chatgpt 4 did great at making queries and finding results, however it wasn't great at outputing responses in a user friendly way. It would often state incorrect facts or interpret the result falsely. I found that doing it the zero-shot had overall the best results as it was less confused and simply excecuted the question asked. With the Multi-shot it struggled to understand what I was wanting and asking even though I gave it some help with added code. Either way chatgpt does help overall in making sql queries, but it is important to recognize and know that the answers it outputs are not always correct. 


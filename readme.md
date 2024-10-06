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

It did find the person who made the most orders and the number, however it didn't specify the name of the person. 

Question: Who has made the most orders?

**GPT SQL Response**:
```sql
SELECT person_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY person_id
ORDER BY total_orders DESC
LIMIT 1;
```

SQL Result the person ID, and count: [(6, 3)]

**Friendly response** "The person with the most orders has made 6 orders."

Here it didn't return the name of person with the most orders, even though I asked who. Which I think would imply the need for a name since we don't reffer to people by numbers. If I had specified I wanted the name it probably could have a result that was more user friendly.



Create table person (
person_id INT auto_increment Primary key,
first_name VARCHAR(25) NOT NULL,
last_name VARCHAR(25) NOT NULL,
birth_date DATE);

Create table email (
email_id INT primary key,
person_id INT NOT NULL, 
email_name VARCHAR(100) NOT NULL,
promo_updates TINYINT NOT NULL,
foreign key (person_id) references person (person_id)
);

CREATE table food_reward (
food_id INT auto_increment Primary key,
food_name VARCHAR(50) NOT NULL unique,
reward_amount INT NOT NULL);


CREATE table orders (
order_id INT auto_increment Primary key,
person_id INT NOT NUll,
food_id INT NOT NULL,
curr_date DATE,
foreign key (person_id) references person (person_id),
foreign key (food_id) references food_reward (food_id)
);

CREATE table reward_total (
person_id INT NOT NULL,
reward_total INT,
number_orders INT,
foreign key (person_id) references person (person_id)
)

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
);

INSERT INTO person (first_name, last_name, birth_date) VALUES
('Charlie', 'Reid', '1985-06-15'),
('Angella', 'Smith', '1990-03-22'),
('Darrel', 'Johnson', '1978-11-02'),
('Sarah', 'Waller', '1995-08-30'),
('David', 'Williams', '2002-12-11');

INSERT INTO email (email_id, person_id, email_name, promo_updates) VALUES
(1, 1, 'charlesried@gmail.com', 1),
(2, 2, 'angellasmith@yahoo.com', 0),
(3, 3, 'darrelj@outlook.com', 1),
(4, 4, 'sarahw@hotmail.com', 1),
(5, 5, 'davidw@gmail.com', 0);

INSERT INTO food_reward (food_name, reward_amount) VALUES
('Chicken Sandwich', 80),
('Chicken Nuggets', 75),
('Waffle Fries', 30),
('Chicken Salad', 60),
('Fruit Side', 40);

INSERT INTO orders (person_id, food_id, curr_date) VALUES
(1, 1, '2024-10-01'),
(2, 2, '2024-10-02'),
(3, 3, '2024-10-03'),
(4, 4, '2024-10-04'),
(5, 5, '2024-10-05');

INSERT INTO reward_total (person_id, reward_total, number_orders) VALUES
(1, 80, 1),
(2, 75, 1),
(3, 30, 1),
(4, 60, 1),
(5, 40, 1);

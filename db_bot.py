import json

import mysql.connector


def read_json():
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config
def connect_to_sql():
    config = read_json()
    db_config = config['mysql']
    connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )

    cursor = connection.cursor()
    return cursor, connection

def create_database(cursor):
    cursor.execute("DROP DATABASE IF EXISTS restaurant_rewards")
    cursor.execute("CREATE DATABASE restaurant_rewards")
    cursor.execute("USE restaurant_rewards")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS person (
        person_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(25) NOT NULL,
        last_name VARCHAR(25) NOT NULL,
        birth_date DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS email (
        email_id INT PRIMARY KEY,
        person_id INT NOT NULL,
        email_name VARCHAR(100) NOT NULL,
        promo_updates TINYINT NOT NULL,
        FOREIGN KEY (person_id) REFERENCES person(person_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_reward (
        food_id INT AUTO_INCREMENT PRIMARY KEY,
        food_name VARCHAR(50) NOT NULL UNIQUE,
        reward_amount INT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        person_id INT NOT NULL,
        food_id INT NOT NULL,
        curr_date DATE,
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY (food_id) REFERENCES food_reward(food_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reward_total (
        person_id INT NOT NULL,
        reward_total INT,
        number_orders INT,
        FOREIGN KEY (person_id) REFERENCES person(person_id)
    )
    """)

    print("Database and tables created successfully!")

# Insert data Into SQL
def insert_data(cursor, connection):
    cursor.execute("""
    INSERT INTO person (first_name, last_name, birth_date) VALUES
    ('Charlie', 'Reid', '1985-06-15'),
    ('Angella', 'Smith', '1990-03-22'),
    ('Darrel', 'Johnson', '1978-11-02'),
    ('Sarah', 'Waller', '1995-08-30'),
    ('David', 'Williams', '2002-12-11'),
    ('John', 'Doe', '1991-01-10'),
    ('Jane', 'Roe', '1988-05-16'),
    ('Michael', 'Smith', '1982-09-25'),
    ('Emily', 'Davis', '1997-12-13'),
    ('Oliver', 'Brown', '2001-04-19'),
    ('Amelia', 'Wilson', '1983-07-22'),
    ('Ethan', 'Taylor', '1999-03-14'),
    ('Sophia', 'Moore', '1992-06-18'),
    ('William', 'Anderson', '1984-11-30'),
    ('Isabella', 'Thomas', '1996-02-28');
    """)

    connection.commit()

    cursor.execute("""INSERT INTO email (email_id, person_id, email_name, promo_updates) VALUES
    (1, 1, 'charlesried@gmail.com', 1),
    (2, 2, 'angellasmith@yahoo.com', 0),
    (3, 3, 'darrelj@outlook.com', 1),
    (4, 4, 'sarahw@hotmail.com', 1),
    (5, 5, 'davidw@gmail.com', 0),
    (6, 6, 'johndoe@gmail.com', 1),
    (7, 7, 'janeroe@hotmail.com', 0),
    (8, 8, 'michael.smith@yahoo.com', 1),
    (9, 9, 'emily.davis@outlook.com', 1),
    (10, 10, 'oliverbrown@gmail.com', 0),
    (11, 11, 'ameliawilson@gmail.com', 1),
    (12, 12, 'ethantaylor@hotmail.com', 0),
    (13, 13, 'sophiamoore@yahoo.com', 1),
    (14, 14, 'william.anderson@gmail.com', 1),
    (15, 15, 'isabellathomas@outlook.com', 0);
    """)

    connection.commit()

    cursor.execute("""INSERT INTO food_reward (food_name, reward_amount) VALUES
    ('Chicken Sandwich', 80),
    ('Chicken Nuggets', 75),
    ('Waffle Fries', 30),
    ('Chicken Salad', 60),
    ('Fruit Side', 40);
    """)

    connection.commit()

    cursor.execute("""INSERT INTO orders (person_id, food_id, curr_date) VALUES
    (1, 1, '2024-10-01'),
    (2, 2, '2024-10-02'),
    (3, 3, '2024-10-03'),
    (4, 4, '2024-10-04'),
    (5, 5, '2024-10-05'),
    (6, 1, '2024-09-15'),
    (6, 3, '2024-09-25'),
    (6, 2, '2024-09-30'),
    (7, 4, '2024-09-22'),
    (8, 2, '2024-09-18'),
    (8, 1, '2024-09-27'),
    (9, 3, '2024-09-16'),
    (9, 4, '2024-09-29'),
    (10, 3, '2024-09-20'),
    (11, 5, '2024-09-28'),
    (12, 2, '2024-09-19'),
    (13, 1, '2024-09-24'),
    (14, 4, '2024-09-23'),
    (15, 5, '2024-09-26');
    """)

    connection.commit()

if __name__ == '__main__':
    cursor, connection = connect_to_sql()
    create_database(cursor)
    insert_data(cursor, connection)

    cursor.close()
    connection.close()
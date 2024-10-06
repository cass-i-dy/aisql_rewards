import mysql.connector


def connect_to_sql():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )

    cursor = connection.cursor()
    return cursor, connection

def create_database(cursor):

    cursor.execute("CREATE DATABASE IF NOT EXISTS my_new_database")

    cursor.execute("USE my_new_database")

    cursor.execute("""
    CREATE TABLE person (
        person_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(25) NOT NULL,
        last_name VARCHAR(25) NOT NULL,
        birth_date DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE email (
        email_id INT PRIMARY KEY,
        person_id INT NOT NULL,
        email_name VARCHAR(100) NOT NULL,
        promo_updates TINYINT NOT NULL,
        FOREIGN KEY (person_id) REFERENCES person(person_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE food_reward (
        food_id INT AUTO_INCREMENT PRIMARY KEY,
        food_name VARCHAR(50) NOT NULL UNIQUE,
        reward_amount INT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        person_id INT NOT NULL,
        food_id INT NOT NULL,
        curr_date DATE,
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY (food_id) REFERENCES food_reward(food_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE reward_total (
        person_id INT NOT NULL,
        reward_total INT,
        number_orders INT,
        FOREIGN KEY (person_id) REFERENCES person(person_id)
    )
    """)

    print("Database and tables created successfully!")


# Insert data Into SQL

def insert_data(cursor):
    cursor.execute("""
    INSERT INTO person (first_name, last_name, birth_date) VALUES
    ('Charlie', 'Reid', '1985-06-15'),
    ('Angella', 'Smith', '1990-03-22'),
    ('Darrel', 'Johnson', '1978-11-02'),
    ('Sarah', 'Waller', '1995-08-30'),
    ('David', 'Williams', '2002-12-11');""")

    cursor.execute("""INSERT INTO email (email_id, person_id, email_name, promo_updates) VALUES
    (1, 1, 'charlesried@gmail.com', 1),
    (2, 2, 'angellasmith@yahoo.com', 0),
    (3, 3, 'darrelj@outlook.com', 1),
    (4, 4, 'sarahw@hotmail.com', 1),
    (5, 5, 'davidw@gmail.com', 0);""")

    cursor.execute("""INSERT INTO food_reward (food_name, reward_amount) VALUES
    ('Chicken Sandwich', 80),
    ('Chicken Nuggets', 75),
    ('Waffle Fries', 30),
    ('Chicken Salad', 60),
    ('Fruit Side', 40);""")

    cursor.execute("""INSERT INTO orders (person_id, food_id, curr_date) VALUES
    (1, 1, '2024-10-01'),
    (2, 2, '2024-10-02'),
    (3, 3, '2024-10-03'),
    (4, 4, '2024-10-04'),
    (5, 5, '2024-10-05');""")

    cursor.execute("""INSERT INTO reward_total (person_id, reward_total, number_orders) VALUES
    (1, 80, 1),
    (2, 75, 1),
    (3, 30, 1),
    (4, 60, 1),
    (5, 40, 1);""")


if __name__ == '__main__':
    cursor, connection = connect_to_sql()
    create_database(cursor)
    insert_data(cursor)

    cursor.close()
    connection.close()
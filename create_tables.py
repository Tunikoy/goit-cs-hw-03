import psycopg2

# Параметри підключення
connection = psycopg2.connect(
    dbname="task_management",
    user="postgres",
    password="",  # Вкажіть пароль, якщо є
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

# SQL-запити для створення таблиць
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""

create_status_table = """
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
"""

create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER REFERENCES status(id) ON DELETE SET NULL,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
"""

# Виконання запитів
cursor.execute(create_users_table)
cursor.execute(create_status_table)
cursor.execute(create_tasks_table)

connection.commit()
cursor.close()
connection.close()

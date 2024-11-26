import psycopg2
from faker import Faker
import random

# Параметри підключення до вашої бази даних
connection = psycopg2.connect(
    dbname="task_management",
    user="postgres",
    password="",  # Якщо пароль не встановлено, залиште порожнім
    host="localhost",
    port="5432"
)

cursor = connection.cursor()
faker = Faker()

# Додавання користувачів
for _ in range(10):
    fullname = faker.name()
    email = faker.unique.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Отримання ID статусів
cursor.execute("SELECT id FROM status")
statuses = [row[0] for row in cursor.fetchall()]

# Отримання ID користувачів
cursor.execute("SELECT id FROM users")
users = [row[0] for row in cursor.fetchall()]

# Додавання завдань
for _ in range(20):
    title = faker.sentence(nb_words=4)
    description = faker.text(max_nb_chars=200)
    status_id = random.choice(statuses)
    user_id = random.choice(users)
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                   (title, description, status_id, user_id))

connection.commit()
cursor.close()
connection.close()

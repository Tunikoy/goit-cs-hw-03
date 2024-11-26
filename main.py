from pymongo import MongoClient, errors

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/") 
db = client['cats_database']  
collection = db['cats']  


def create_cat(name, age, features):
    """Створення нового запису (кота) в базі даних."""
    try:
        new_cat = {"name": name, "age": age, "features": features}
        collection.insert_one(new_cat)
        print(f"Кота {name} успішно додано.")
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні кота: {e}")


def read_all_cats():
    """Виведення всіх записів у колекції."""
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except errors.PyMongoError as e:
        print(f"Помилка при читанні даних: {e}")


def find_cat_by_name(name):
    """Пошук кота за ім'ям."""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при пошуку кота: {e}")


def update_cat_age(name, new_age):
    """Оновлення віку кота за ім'ям."""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Вік кота {name} оновлено до {new_age}.")
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні віку: {e}")


def add_feature_to_cat(name, new_feature):
    """Додавання нової характеристики до списку features кота."""
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"До кота {name} додано нову характеристику: {new_feature}.")
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні характеристики: {e}")


def delete_cat_by_name(name):
    """Видалення запису за ім'ям."""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кота {name} видалено.")
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні кота: {e}")


def delete_all_cats():
    """Видалення всіх записів у колекції."""
    try:
        collection.delete_many({})
        print("Усі записи видалено.")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні записів: {e}")


# Меню для тестування
if __name__ == "__main__":
    while True:
        print("\n--- Меню ---")
        print("1. Додати кота")
        print("2. Вивести всіх котів")
        print("3. Знайти кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("0. Вийти")
        choice = input("Оберіть дію: ")

        if choice == "1":
            name = input("Ім'я кота: ")
            age = int(input("Вік кота: "))
            features = input("Характеристики (через кому): ").split(", ")
            create_cat(name, age, features)
        elif choice == "2":
            read_all_cats()
        elif choice == "3":
            name = input("Введіть ім'я кота: ")
            find_cat_by_name(name)
        elif choice == "4":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Новий вік: "))
            update_cat_age(name, new_age)
        elif choice == "5":
            name = input("Введіть ім'я кота: ")
            new_feature = input("Нова характеристика: ")
            add_feature_to_cat(name, new_feature)
        elif choice == "6":
            name = input("Введіть ім'я кота: ")
            delete_cat_by_name(name)
        elif choice == "7":
            delete_all_cats()
        elif choice == "0":
            print("Вихід.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

# будем добавлять юзеров в users.json
# { пример
#     "user1": {
#         "name": "John",
#         "surname": "Doe",
#         "age": 30,
#         "city": "New York"
#     }
# }
# def add_user(filename, name: str, surname: str, age: int, city: str):
#     if not all(isinstance(x, t) for x, t in [(name, str), (surname, str), (age, int), (city, str)]):
#         return False 
# как вариант проверки от чат гпт

import json

def add_user (filename, name: str, surname: str, age: int, city: str, user_name: str):
    #на всякий случай проверку на правильность входных данных
    if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(age, int) or not isinstance(city, str):
        return False

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    data[user_name] = {}

    data[user_name]["name"] = name
    data[user_name]["surname"] = surname
    data[user_name]["age"] = age
    data[user_name]["city"] = city

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
def enter_str(str: str):
    while True:
        enter_word = input(f"Enter your {str}: ")
        return enter_word
        break
def enter_num(num: str):
    while True:
        try:
            enter_number = int(input(f"Enter your {num}: "))
            return enter_number
            break
        except ValueError:
            print("Invalid input")

filename = "files/users.json"

name = enter_str("name")
surname = enter_str("surname")
age = enter_num("age")
city = enter_str("city")

add_user(filename, name, surname, age, city, "user3")
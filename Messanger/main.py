account = {
    "name": "Name",
    "surname": "Surname",
}


def change_name(*, person):
    name = input("Enter your new name: ")
    person["name"] = name
    surname = input("Enter your new surname: ")
    person["surname"] = surname


def add_to_history(*, text):
    with open('MesFile/history.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')


while True:
    print("Welcome to Messanager!")
    changing = input("Would you like to change your name? (y/n): ").lower()
    if changing == "y":
        change_name(person=account)
    elif changing == "n":
        break
    else:
        print("Invalid input. Please \"y\" or \"n\"")

while True:
    y_or_n = input("Do you want to type message? (y/n): ").lower()
    if y_or_n == "y":
        message = input("Type your message: ")
        add_to_history(text=message)
    elif y_or_n == "n":
        break
    else:
        print("Invalid input. Please \"y\" or \"n\"")

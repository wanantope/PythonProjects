account = {
    "name": "Name",
    "surname": "Surname",
}


def change_name(*, person):
    name = input("Enter your new name: ")
    person["name"] = name
    surname = input("Enter your new surname: ")
    person["surname"] = surname


change_name(person=account)
print(account)

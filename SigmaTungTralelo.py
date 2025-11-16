from random import randint

number = randint(1, 3)

print("Э, слышь тыэ, угадэй числе!")

a = int(input("Введите число от 1 до 3: "))

if a == number:
    print("Вы угадали число!", number)
else:
    print("Вы дэбил, который не угадал число", number)

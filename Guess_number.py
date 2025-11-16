import random

r_number = random.randint(1, 10)
attempts = 1
while True:
    try:
        answer = int(input("Guess a number 1-10: "))
        if answer == r_number:
            print(f"You guess a number {r_number}!")
            print(f"You got it in {attempts} attempts!")
            break
        if answer != r_number:
            print("Try again!")
            attempts += 1
            continue

    except ValueError:
        print("That's not a number. Try again!")
        continue

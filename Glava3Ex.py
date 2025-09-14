guests = ["Papa", "Mama", "Granny", "Grandpa", "Friend", "Sister", "Dog", "Worker", "Bird", "Ilon Mask", "Marsian"]
for i in range(len(guests)):
    print(f"Hello {guests[i]}, do you want to have dinner with all?")

cantCome = guests.pop(-3)
print(f"{cantCome} cant come.")
guests.insert(-3, "Eagle")
print()
for i in range(len(guests)):
    print(f"Hello {guests[i]}, do you want to have dinner with all?")

print()
index = int(len(guests)/2)
guests.insert(index, "Sigma")

index = int(len(guests)/2)
guests.insert(index, "Alpha")

index = int(len(guests)/2)
guests.insert(index, "Delta")
for i in range(len(guests)):
    print(f"Hello {guests[i]}, do you want to have dinner with all?")

print()

x = len(guests)

while x > 2:
    guests.pop()
    x -= 1

for i in range(len(guests)):
    print(f"Hello {guests[i]}, last invite is actually")

print()
birds = ["Синица", "Воробей", "Попугай"]
for bird in birds:
    print(f"{bird} это птица.")
    print("Она может летать.")
    print()

nums = [num**3 for num in range(1, 900)]
print(nums)

pcici = birds[:] #можно использовать срезы для выбора фрагмента для копирования
print(pcici)

korteg = ("sigma", "amgis", "tuple")
print(korteg)
korteg = list(korteg)
korteg.append("apple")
korteg = tuple(korteg)
print(korteg)

while True:
    while True:
        if 0 == 0:
            print("Skebob")
            break
        if 0 == 1:
            print('Sinkers')
    print("Sigma")
    break
print("Delta")
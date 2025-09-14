pl = ["python", "java", "c", "go", "php"]
print("Original array")
for x in pl:
    print(x.title())

pl.append("pascal")
print("\nAppend word in array")
for x in pl:
    print(x.title())

pl.insert(0, "c++")
print("\nInsert word in array")
for x in pl:
    print(x.title())

del pl[-2]
print("\nDelete \"Php\" in array")
for x in pl:
    print(x.title())

pl.pop() #delete last lang
print("\nDelete last element with .pop()")
for x in pl:
    print(x.title())

pl.pop(2) #delete java lang
print("\nDelete \"Java\" with .pop()")
for x in pl:
    print(x.title())

dude = pl.pop(1)
print(f"\nIt is a {dude} dude |?_?|")

pl.remove("c++")
print("\nDelete \"C++\"")
for x in pl:
    print(x.title())

print()

SimpleWord = "Sigma"
print("Original word:", SimpleWord)
print("Срезы слова:", SimpleWord[-1:0:-1])

print()
arraysk = ["bebek","abek", "cebikek"]
print("Original array:", arraysk)
print("Edited array:", sorted(arraysk), "времено метод sorted(arraysk)") #времено
print("Original array:", arraysk)
arraysk.sort
print("Edited array:", arraysk, "метод sort")
print("Original array:", arraysk)
arraysk.reverse()
print("Edited array:", arraysk, "развернут методом .reverse()")
length = len(arraysk)
print(length, " - длина списка")

print()
numbers = list(range(1, 50+1))
print(numbers)

print()
arr = [value*2 for value in range(1, 11)]
print(arr)

print()
nums = [value for value in range(1, 1_000_001)]
sum = 0
for num in nums:
    sum += num
print()
print(sum)


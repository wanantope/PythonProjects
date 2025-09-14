def isEven(n):
    return n//2 if n % 2 == 0 else 3*n+1
number = int(input("Enter number: "))
print(isEven(number))
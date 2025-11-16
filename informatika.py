# def kdn(number):
#     count = 0
#     number = str(number)
#     for nums in number:
#         count += 1
#     return count
#
#
# num = int(input("Enter a number: "))
# print(kdn(num))
#

def f(n):
    if n <= 1:
        return 0
    if n % 2 == 1 and n > 1:
        return f(n - 1) + 3 * n ** 2
    elif n % 2 == 0 and n > 1:
        return n / 2 + f(n - 1) + 2


print(f(49))

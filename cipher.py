def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def square(num):
    return num ** 2

num = int(input("Enter the number: "))

for i in range(1, num):
    result = square(i) / factorial(i)
    print(result)



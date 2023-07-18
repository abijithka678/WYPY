'''
Write a Python Program to display the sum of odd numbers between a programmer specified upper and lower limit
'''
lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))
sum = 0
for i in range(lower,upper+1):
    if i%2 !=0:
        print("Number takes for addition are "+ str(i))
        sum = sum+i
print("Sum of numbers of odd numbers are : "+ str(sum))
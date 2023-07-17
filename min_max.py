'''
Create a function min_max that takes n numbers as list argument and return the smallest and largest numbers
'''

list = []
def min_max(n):
    list.append(n)

num = int(input("Enter the number of input :"))
for i in range(num):
    n = int(input("Enter the values : "))
    min_max(n)
print("Maximum value in the list "+ str(max(list)))
print("Minmum value in the list "+ str(min(list)))
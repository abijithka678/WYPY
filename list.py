'''
Enter numbers into the list and split that number into two seperate list with positive and negeative list
'''
limit = int(input("Enter the limit of the numbers :"))
list = []
positive =[]
negative =[]
for i in range(limit):
    num = int(input("Enter a number :"))
    list.append(num)

print(list)
for i in range(limit):
    if list[i]<0:
        negative.append(list[i])
    else:
        positive.append(list[i])
print(negative)
print(positive)


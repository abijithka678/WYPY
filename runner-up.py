'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.
Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
'''
num = int(input("Enter the number :"))
score =[]
for i in range(num):
    values = int(input("Enter the values:"))
    score.append(values)
print(score)
list_sort = sorted(score)
print(list_sort)
length = len(list_sort)
print("Runner-up is "+str(list_sort[length-2]))
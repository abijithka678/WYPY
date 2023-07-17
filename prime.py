'''
Find the Prime numbers between 1 and 1000 using python program
'''
#Used to print the start state of time
import datetime
timming = datetime.datetime.today()
print(timming)
for i in range(1,1001):
    for j in range(2,i):
        if i%j == 0:
            break;
        else:
            print("This is a prime number" + str(i))
timming = datetime.datetime.today()
print(timming)
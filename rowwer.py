'''
Write a python program to generat the following type of pattern for the N number of rows:
1
12
123
1234
'''
import datetime
dati = datetime.datetime.today()
print("Starting of Program :"+str(dati))
row = int(input("Enter the number of row : "))
for i in range(row):
    for j in range(i+1):
        print(j+1,end ='')

    print()
dati2 = datetime.datetime.today()
print("After complete of program :"+str(dati2))
diff = dati2 - dati
print("Difference between the timming : "+str(diff))
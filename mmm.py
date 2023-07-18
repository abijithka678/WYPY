'''
Write a python program to create a set of functions that compute the mean,median and mode
of a set of numbers.Each function should expect a list of numbers as an argument and return a single numbers.
Each function should return 0 if the list is empty.Include a main function that test the three functions with a given list.
'''
listin = [1,2,3,8,4,2]
med =[]
class mmm:

    def average(self,listin):
        sum = 0
        max = len(listin)
        for i in listin:
            sum = sum + i

        avg = sum / max
        avg = int(avg)
        print("Average of list : " + str(avg))




    def median(self,listin):
        self.listin = listin
        lst_sorted = sorted(self.listin)
        print(lst_sorted)
        length = len(lst_sorted)
        print(length)
        if length%2 ==0:
            mid = length/2

            mid = int(mid)


            median = lst_sorted[mid]+lst_sorted[mid-1]

            print("Median of the given list "+str(median))
        else:
            mid = length/2
            print(mid)
            mid = int(mid)

            median = lst_sorted[mid]
            print("Median for the given list "+str(median))


x= mmm()
x.median(listin)
x.average(listin)
'''
Create an abstract class with abastract method area and inherit in on another class to implement the abstract method
'''

import datetime

begin = datetime.datetime.today()
print(begin)
from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class rectangle(Shape):

    def area(self):
        length = int(input("Enter the length of rectangle : "))
        breadth = int(input("Enter the breadth of rectangle :"))
        area = length * breadth
        print("Area of Rectangle is "+ str(area))

x = rectangle()
x.area()

end = datetime.datetime.today()
time_taken = end - begin
print("Token time taken to execute the above piece of code :"+ str(time_taken))
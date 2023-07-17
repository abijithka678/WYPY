'''
Create a dictonary of names and birthdays.Wrie a python program that asks the user to enter a name and the program display the birthday of that person.
'''
dict = {
    "name" : "Abijith",
    "birthday" : "19/02/2002"
}

name = input("Enter a name :")
if dict["name"].lower() == name.lower():
    print(dict["birthday"])
else:
    print("you are a fool")
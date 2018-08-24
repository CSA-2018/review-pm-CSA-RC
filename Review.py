# Ryan Callahan
# Computer Programming Sixth Period
# 8-22-18


class Person:
    def __init__(self, name, age, city, phoneNum):
        self.name = name
        self.age = age
        self.city = city
        self.phoneNum = phoneNum
    def __str__(self):
        return f"{self.name} is {self.age} years old, lives in {self.city}, and their phone number is {self.phoneNum}."

def start():
    username = input("What is your name? ")
    userage = input("How old are you? ")
    usercity = input("What city do you live in? ")
    userphonenum = getphone()
    p1 = Person(username, userage, usercity, userphonenum)
    print(p1)

def getphone():
    try:
        userphonenum = int(input("What is your phone number? "))
        return userphonenum
    except ValueError:
        print ('Thats not a number! ')
        getphone()

start()

'''
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into
MyClass.method(myobject, arg1, arg2) – this is all the special self is about. 
'''

class Company:
    def __init__(self,name,company):
        self.name=name
        self.company=company

    def show(self):
        print("Hello my name is " +self.name +" I work in " +self.company)

name=input()
comp=input()
Com=Company(name,comp)
Com.show()

'''
The Self Parameter does not call it to be Self, You can use any other name instead of it. Here we change the self to the word someone and the 
output will be the same.
'''

class Car:
    def __init__(c,name,company):
        c.name=name
        c.company=company

    def show(c):
        print("Hello my Car name is " +c.name +" I work in " +c.company)

name=input()
comp=input()
Com=Company(name,comp)
Com.show()
'''
In this example, we created the object ‘obj’ of the child class. When we called the constructor of the child class ‘Student’, 
it initialized the data members to the values passed during the object creation. Then using the super() function, we invoked the 
constructor of the parent class.

Python3
'''

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
            print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age):
        self.sName=name
        self.sAge=age

        # inheriting the properties of parent class
        super().__init__(name, age)

    def displayInfo(self):
        print(self.sName, self.sAge)

n=input()
age=int(input())
obj=Student(n,age)
obj.display()
obj.displayInfo()
    
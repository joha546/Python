'''
One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy 
of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive 
or inherit the properties from another class. 

Benefits of inheritance are:

Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class. The benefits of Inheritance in 
Python are as follows:

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class 
without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit 
from class A.
Inheritance offers a simple, understandable model structure. 
Less development and maintenance expenses result from an inheritance. 
'''

# Creating a Base class
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(self.name, self.id)

emp=Person("Satyam",102)
emp.display()


# Creating a Child Class

class Emp(Person):
    def Print(self):
        print("Emp class called")

Emp_details=Emp("Manyak", 103)
Emp_details.display()

Emp_details.Print()
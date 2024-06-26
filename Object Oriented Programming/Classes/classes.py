''''
A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together.
 Creating a new class creates a new type of object, allowing new instances of that type to be made. 
 Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) 
 for modifying their state.

 The class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by 
 creating an instance of that class. A class is like a blueprint for an object.

 Some points on Python class:

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute
'''

# Creating Class
'''
class Dog:
    sound="bark"'''

'''
Object of Python Class
An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values. It’s not an idea anymore,
 it’s an actual dog, like a dog of breed pug who’s seven years old. You can have many dogs to create many different instances, 
 but without the class as a guide, you would be lost, not knowing what information is required.

An object consists of:

State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.
'''

class Dog:
    attr1='mammal'
    attr2='dog'

    def fun(self):
        print("I am a ",self.attr1)
        print("I am a",self.attr2)

Rodger=Dog()     # Object instantiation
print(Rodger.attr1)
Rodger.fun()



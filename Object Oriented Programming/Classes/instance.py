class Dog:
    animal='dog'

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color


Rodger=Dog("Pug","brown")
Buzo=Dog("Bulldog","black")

print("Rodger Details")
print("Rodger is a ", Rodger.animal)
print("Breed:",Rodger.breed)
print("Color is:",Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)
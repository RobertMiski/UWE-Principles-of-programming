"""
So far you have been coding in a procedural paradigm meaing top down like a set of intructions.
Object oriented paradigm is different and works by creating objects and using then to interact this way your code can jump around and be more complex.
Objects in computer science is basicly writing a blue print to try and recreate something from real life.
All object will have a name, attributes (variables) and behaviours (functions).

all video games use Object oriented programming to create them.

Attributes will be the variables held in the class you are able to have static and dynamic attributes, the static attributes will effect every object of that class
and the dynmic will only effect each instance of the class created same goes for behaviours.

In python to create a object we use the key word class
"""

class Animal:
    # static attributes are created like this outside of the __init__ function
    staticAttribute = 10

    # __init__ is the first function to run once you create an object
    # self is how we create attributes all being dynamic
    # you can pass in arguemtns to the __init__ function to set the attributes right at the beggin or if none a passed 100 will de default.
    def __init__(self, health = 100, hunger = 100):
        self.health = health
        self.hunger = hunger
        self.isSleeping = False
        self.isEating = False
        self.isAlive = True

    # by convention we use setters and getter to change attributes this stop any accidental changes this also count as behaviours
    # setters
    def setHealth(self, amount):
        self.health += amount
        self.CheckHealth()

    def setHunger(self, amount):
        self.hunger += amount

    def setIsSleeping(self, state):
        self.isSleeping = state

    def setIsEating(self, state):
        self.isEating = state

    def setIsAlive(self, state):
        self.isAlive = state

    # getters
    def getHealth(self):
        return self.health
    def getHunger(self):
        return self.hunger
    def getIsSleeping(self):
        return self.isSleeping
    def getIsEating(self):
        return self.isEating
    def getIsAlive(self):
        return self.isAlive

    # behaviours
    def CheckHealth(self):
        if(self.health == 0 or self.health < 0):
            self.isAlive = False


def main():
    # to create an instance of the object animal
    # seeing <__main__.Animal object at {hexcode e.g 0x00AC8148}> is the object
    # then 100 for the health of the aniaml
    
    animal  = Animal()
    print(animal)
    print(animal.getHealth())

# start of the programme
if __name__ == "__main__":
    main()
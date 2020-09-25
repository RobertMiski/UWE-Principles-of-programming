"""
In Object oriented programming there is concept called Inheritance this acts like a gentic tree like how you inherent you eye colour from you parents.
One class can inherent from another class meaning all methods that are public are there for the new class to use.
Sometimes called Superclass and Subclass
"""

# class from file 1 - 1 - classes-objects-&-basics.py
class Animal:
    staticAttribute = 10

    def __init__(self, health = 100, hunger = 100):
        self.health = health
        self.hunger = hunger
        self.isSleeping = False
        self.isEating = False
        self.isAlive = True

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


class Dog(Animal):
    
    # initialises the animal class so we can have access to all of the attributes and methods
    # we can also add extra attributes and methods on top that only the cat objects can use

    def __init__(self, hunger=100):
        super().__init__(health=130, hunger=hunger) # all dog object will have a starting health of 130
        self.coatColour = "black"
        self.eyeColour = "green"
        self.speed = 10

    #setters
    def setEyeColour(self, colour):
        self.eyeColour = colour

    def setCoatColour(self, colour):
        self.coatColour = colour

    def setSpeed(self, speed):
        self.speed = speed

    #getters
    def getEyeColour(self):
        return self.eyeColour
    def getCoatColour(self):
        return self.coatColour
    def getSpeed(self):
        return self.speed

    # behaviours

    def Run(self):
        self.speed = 20
    def Walk(self):
        self.speed = 10


def main():
    # the dog object has access to all public attributes and methods in both the animal and dog class
    dog = Dog()
    print(dog.getEyeColour(), dog.getHealth())

if __name__ == "__main__":
    main()
"""
static and dynamic is a way of explaning how the attributes are interated with.
static attributes effect every instance of the class where dynamic on effects a single instance.
dynamic attributes are initilised in the __init__ function and static a created outside at the begging of the class.
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

def main():
    # to access a static attribute on a class 
    print(Animal.staticAttribute)
    Animal.staticAttribute = 5
    print(Animal.staticAttribute)

def main2():
    # accessing any dynamic attribute you need an instance then directily chnage the attribute on the instance
    animal = Animal(120, 75)
    print(animal.getHealth())

if __name__ == "__main__":
    main()
    # main2()
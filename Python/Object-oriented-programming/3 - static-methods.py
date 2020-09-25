# class from file 1 - 1 - classes-objects-&-basics.py but added  static method
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

    # static method using the @staticmethod decoration 
    @staticmethod
    def staticMethod():
        Animal.staticAttribute = 50

def main():
    # changing the static attribute using a static method this static method cann't be called on an instance but on the class it self
    animal1 = Animal()
    animal2 = Animal()

    Animal.staticMethod()
    print(animal1.getHealth(), animal2.getHealth())


if __name__ == "__main__":
    main()
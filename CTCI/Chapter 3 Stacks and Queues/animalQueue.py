class Animal:
    order = -1
    name = ''

    def __init__(self, order, name):
        self.order = order
        self.name = name

class AnimalQueue:
    dogs = []
    cats = []
    order = 0

    def addDog(self, name):
        animal = Animal(self.order, name)
        self.order += 1
        self.dogs.append(animal)

    def addDog(self, name):
        animal = Animal(self.order, name)
        self.order += 1
        self.cats.append(animal)

    def dequeueDog(self):
        return self.dogs.pop(0).name

    def dequeueCat(self):
        return self.cats.pop(0).name
    
    def dequeueAny(self):
        firstCat = self.cats[0]
        firstDog = self.dogs[0]
        if firstCat.order < firstDog.order:
            return self.cats.pop(0)
        else:
            return self.dogs.pop(0)

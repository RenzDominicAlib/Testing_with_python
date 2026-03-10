from Animals import Animal


class Mammal(Animal):
    def __init__(self,name, breed, petType):
        Animal.__init__(self, name, breed, petType)
        self.breed = breed
        self.name = name
        self.petType = petType

Pet1 = Mammal('Doggy', 'Shihtzu', 'Dog')
print(Pet1.identification())

Pet2 = Mammal('Meowy', 'Persian', 'Cat')
print(Pet2.identification())
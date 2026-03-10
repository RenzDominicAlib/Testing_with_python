class Animal:
    def __init__(self, name, breed, petType):
        self.name = name
        self.petType = petType
        self.breed = breed

    def breed(self):
        return f'My breed is {self.breed}'

    def identification(self):
        return f'Hi hooman! My name is {self.name}!. \n Iam a {self.breed} {self.petType}.'

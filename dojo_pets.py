'''
Create: Ninja class and Pet class
Ninjas: able to have a pet
'''
class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 50
        self.noise = noise
    
    def sleep(self):
        self.energy = self.energy + 25
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        return self

    def play(self):
        self.health = self.health + 5
        self.energy = self.energy - 10
        return self

    def noise(self):
        print(self.noise)
        

    def pet_status(self):
        print(f"Name: {self.name} Type: {self.type} Tricks: {self.tricks} Health: {self.health} Energy: {self.energy} Noise: {self.noise}")
        return self


pet_treats = ["milkbones", "beggin-bits"]
pets_food = ["dry-food", "wet_food"]


lily = Pet("lily", "tabby-cat", "4 am laps", "MEOWWW!")
lauren = Ninja("Lauren", "Clise", lily, pet_treats, pets_food)

jesse = Pet("Jesse", "red-lab", "sit and shake!", "WOOF!")
jake = Ninja("Jake", "Clise", jesse, pet_treats, pets_food)

jake.feed().walk()
jesse.pet_status()

jesse.play()
jesse.pet_status()
print(jesse.noise)

lauren.feed().walk()
lily.pet_status()
print(lily.noise)








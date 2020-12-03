import pickle


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Floyd", "String")
with open("cats.pickle", "wb") as f:
    pickle.dump(blue, f)
    print("Dumped pickle")

with open("cats.pickle", "rb") as file:
    new_blue = pickle.load(file)
    print(new_blue)
    new_blue.play()
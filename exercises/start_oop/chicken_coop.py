"""
    Create Chicken class, Each Chicken has a species and a name, as well as eggs. Eggs always start at 0.

    Each chicken can lay_egg(), lay_egg()increments and returns that chicken's eggs. The whole coop (Chicken) have total_eggs
"""


class Chicken:
    total_eggs = 0

    def __init__(self, species, name):
        self.eggs = 0
        self.species = species
        self.name = name

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")

print(c1.lay_egg())  # should be 1
print(Chicken.total_eggs)
print(c2.lay_egg())
print(c2.lay_egg())

print(Chicken.total_eggs)

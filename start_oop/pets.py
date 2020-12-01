"""
    Code along
"""


class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        self.name = name
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.species = species

    def set_species(self, species):
        """ Set species if the species is in Pet.allowed """
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

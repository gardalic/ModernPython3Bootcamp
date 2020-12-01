"""
    Create a class Train that has one attribute: num_cars which is specified when Train is instantiated.
    There should be two special methods under it:
    1. one method that describes the train when we call print on it
        - x car train
    2. one method that denotes the length of the train when we call len on it
"""


class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return f"{self.num_cars} car train"

    def __len__(self):
        return int(self.num_cars)

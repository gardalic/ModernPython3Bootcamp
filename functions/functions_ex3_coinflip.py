# Coin flip with functions

from random import random


def flip_coin():
    # generate number from 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"


print(flip_coin())

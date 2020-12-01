"""
    Your task is to simply print out a string depending on if food is a value in bakery_stock. If food is contained in bakery_stock print out a string that states how many items are left: "3 left" if food is "toffee cookie" "1 left", etc. If food is not contained in bakery_stock  (like "gummy bear"), print out "We don't make that"
"""
# This code picks a random food item:
from random import choice  # DON'T CHANGE!
food = choice(["cheese pizza", "quiche", "morning bun",
               "gummy bear", "tea cake"])  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print(f"{food}: {bakery_stock[food]} left")
else:
    print(f"We don't make that ({food})")

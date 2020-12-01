# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, 'Both numbers must be positive!'
#     return x + y

def eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
    ], "Food must be a junk food"
    return f"NOM NOM NOM, I am eating {food}"


food = input("Enter a food please: ")

print(eat_junk(food))

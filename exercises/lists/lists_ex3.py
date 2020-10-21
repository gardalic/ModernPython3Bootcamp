"""
    Loop over the list, add the elements together and convert them to uppercase.
    The result should be in a single variable (result).
"""

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ""

for elem in sounds:
    result += elem.upper()

print(result)

"""Write a function called parse_bytes  that accepts a single string.  It should return a list of the binary bytes contained in the string.  
Each byte is just a combination of eight 1's or 0's. For example:
parse_bytes("11010101 101 323")    # ['11010101']
parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']
parse_bytes("asdsa")   # []"""
import re

def parse_bytes(input):
    pattern = re.compile(r"\b[10]{8}\b") # [10] regex, checks for 1 or 0
    return pattern.findall(input)

print(parse_bytes("11010101 101 323")) # ['11010101']
print(parse_bytes("my data is: 10101010 11100010")) # ['10101010', '11100010']
print(parse_bytes("asdsa")) # []

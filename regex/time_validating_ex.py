"""Write a function called is_valid_time  that accepts a single string argument.  It should return True  if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.  Note that times can start with a single number (2:30) or two (11:18). """

import re

def is_valid_time(input) -> bool:
    pattern = re.compile(r"\d{1,2}:\d{2}")
    match = pattern.fullmatch(input)
    if match:
        return True
    return False

print(is_valid_time("it is 12:10"))
print(is_valid_time("11:34"))
print(is_valid_time("4:2"))
print(is_valid_time("4:21"))
print(is_valid_time("114:21"))

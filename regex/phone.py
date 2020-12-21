import re

def extract_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.findall(input)
    return match # findall() returns the values right away


# def is_valid_phone(input) -> bool:
#     phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False

def is_valid_phone(input) -> bool:
    phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False

print(extract_phone("my number is 432 567-8976"))
print(extract_all_phones("my numbers are 455 567-8975 and 432 567-1337"))

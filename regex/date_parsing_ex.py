"""Define a function called parse_date  that accepts a single string.  Your code should check to see if the string
matches a date format. We're going to use the DMY format of "dd/mm/yyyy", but it should also work with "dd.mm.yyyy"
and "dd,mm,yyyy". If you are American, note that Day if before Month! However, rather than simply returning True or
False if the string matches...you should instead return a dictionary containing the three parts of the date with the
keys "d", "m" , and "y" """
import re


def parse_date(date_in):
    pattern = re.compile(r"^([0-9]{2})[.,/]([0-9]{2})[.,/]([0-9]{4})$")
    match = pattern.search(date_in)
    if match:
        return {"d": match.group(1), "m": match.group(2), "y": match.group(3)}
    return None


print(parse_date("12.11.2003"))
print(parse_date("12,04,2003"))
print(parse_date("12.11.200312"))

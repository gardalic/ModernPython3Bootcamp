"""
    Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).

    - If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
    - If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
    - If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
    - If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list
"""
lst = []
lst.insert
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "beginning":
            return lst.pop(0)
        elif location == "end":
            return lst.pop()
    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.insert(len(lst), value)
            return lst


print(list_manipulation([1, 2, 3], "remove", "end"))
print(list_manipulation([1, 2, 3], "remove", "beginning"))
print(list_manipulation([1, 2, 3], "add", "beginning", 20))
print(list_manipulation([1, 2, 3], "add", "end", 30))

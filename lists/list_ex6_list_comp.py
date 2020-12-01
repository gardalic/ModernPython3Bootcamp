"""
    Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list 
    containing the first letter of each name in the list.  
    I would use a list comprehension, though you could also loop over manually.
"""
# Second problem
"""
    Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.  
    Another good candidate for a list comp.
"""
list1 = ["Elie", "Tim", "Matt"]

answer = [letter[0] for letter in list1]
print(answer)

list2 = [1,2,3,4,5,6]

answer2 = [x for x in list2 if x % 2 == 0]
print(answer2)

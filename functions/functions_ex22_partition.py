"""
    Write a function called partition. This function accepts a list and a callback function (which you can assume returns True or False. The function should iterate over each element in the list and invoke the callback function at each iteration. 

    If the result of the callback function is True, the element should go into the first list (i.e. the "truthy" list).
    If the result of the callback function is False, the element should go into the second list (i.e. the "falsy" list).

    When it's finished, partition should return both lists inside of one larger list.
"""
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def isEven(num):
    return num % 2 == 0


def partition(lst, function):
    truthy = []
    falsey = []

    for elem in lst:
        if function(elem):
            truthy.append(elem)
        else:
            falsey.append(elem)

    return [truthy, falsey]


print(partition([1, 2, 3, 4], isEven))

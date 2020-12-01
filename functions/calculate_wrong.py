"""
    Oh boy, this is a complicated set of instructions.  Bear with me. Write a function called calculate that accepts a list of keyword arguments
    - make_float, a boolean which returns a float if True or an integer if False.
    - operation which is either 'add', 'subtract', 'multiply', and 'divide'. 
    - first  which is a number, second , which is another number, and message which is a string that can be added. The function should return the result of actually running the specified operation with the first and second keyword arguments. The result of the operation with the first and second is an integer if the make_float  keyword argument is False , otherwise the result of the operation is a float. If a message is specified, it should return the message keyword argument + the result of the operation.  Otherwise, it should return the string  "The result is " joined with the result of the operation.See the examples below for some more information. Remember, you can't use f-strings on in the Udemy Editor.
"""
'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**kwargs):
    result = 0  # kwargs['first']
    message = ""
    if 'message' in kwargs: 
        message = str(kwargs['message'])
    else: 
        message = ""

    if kwargs['operation'] == 'add':
        # really need to do a check here
        result = kwargs['first'] + kwargs['second']
    elif kwargs['operation'] == 'subtract':
        result = kwargs['first'] - kwargs['second']
    elif kwargs['operation'] == 'divide':
        result = kwargs['first'] / kwargs['second']
    elif kwargs['operation'] == 'multiply':
        result = kwargs['first'] * kwargs['second']
    else:
        # Need to escape this for float
        result = "Invalid operation"

    if kwargs['make_float'] == True:
        result = float(result)
    else:
        result = int(result)

    return message + str(result)


print(calculate(make_float=True, operation='divide', first=3.5, second=5))

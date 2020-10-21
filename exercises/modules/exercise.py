"""
    Your task is to write a function in the helpers.py file, and then call it from the exercise.py file.  More specifically:
    1. In helpers.py,  define a function called lucky_number()  that always returns the number 37.  That's it.   It always returns 37, no matter what.
    2. In exercise.py, import the helpers module.  In order for the testing logic to work properly, don't use the 'as', or  keywords when importing.  Just do a plain old import.
    3. From inside exercise.py, call the lucky_number  function you defined in the helpers module. Save the result to a variable called num

    The point of this exercise is to get comfortable working with multiple files, and defining custom modules.   Because of that, the testing logic actually checks to see that your code is all in the correct filed rather than just checking if you got the right answer.
"""
import helpers

num = helpers.lucky_number()

print(num)

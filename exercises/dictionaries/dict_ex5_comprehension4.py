"""    
    Your task is to create dictionary that maps ASCII keys to their corresponding letters.  Use a dictionary comprehension and chr(). Save the result to the answer variable. You only need to care about capital letters (65-90).
"""
# make sure your solution is assigned to the answer variable so the tests can work!
answer = {i: chr(i) for i in range(65, 91)}
print(answer)

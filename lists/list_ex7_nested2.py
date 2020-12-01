"""
    Using list comprehension, create a variable called "answer" with a 10x10 nested list. 10 rows, each row contains the numbers 0-9. 
"""
answer = [[i for i in range(0,10)] for j in range(0,10)]
for i in answer:
    print(i)

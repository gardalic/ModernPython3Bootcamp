"""
    Write a function called yes_or_no, which returns a generator that first yields yes , then no, then  yes , then no, and so on
"""


def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        answer = 'no' if answer == 'yes' else 'yes'


gen = yes_or_no()

print(next(gen))  # 'yes'
print(next(gen))  # 'no'
print(next(gen))  # 'yes'
print(next(gen))  # 'no'

"""   
    Create a dictionary called "answer", that makes each first item in each list a key and the second item a corresponding value. That's a terrible explanation. I think it'll be easier if you just look at the end goal:  {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
"""

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {info[0]: info[1] for info in person}

print(answer)

# OR can do
answer = {k: v for k, v in person}  # better
print(answer)

# OR EVEN
answer = dict(person)  # simple
print(answer)

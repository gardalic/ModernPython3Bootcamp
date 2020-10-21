"""
    I'm having a party, and made a list of people I want to invite.  Unfortunately, I'm a terrible friend and made a couple of spelling errors.  Help me correct them!
        1 - Change "Hanna" to "Hannah" (there should be an 'h' at the end)
        2 - Change "aparna" to "Aparna" (capitalize it)
        3 - Change "Geoffrey" to "Jeffrey"
"""

# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

for person in range(0, len(people)):
#Change "Hanna" to "Hannah"
    if people[person] == "Hanna":
        people[person] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
    if people[person] == "Geoffrey":
        people[person] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
    if people[person] == "aparna":
        people[person] = people[person].capitalize()

print(people)

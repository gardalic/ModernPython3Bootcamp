import requests
# from random import randint # Can do choice()
from random import choice

url = "https://icanhazdadjoke.com/search"
src_term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params={"term": f"{src_term}"}
                        ).json()

if len(response['results']) == 1:
    print(
        f"I only have one joke about '{src_term}', here it is: \n{response['results']['joke']}")
elif len(response['results']) > 1:
    print(
        f"I have {len(response['results'])} jokes about '{src_term}', here is one: \n{choice(response['results'])['joke']}")
else:
    print(f"I don't have any jokes about '{src_term}'")

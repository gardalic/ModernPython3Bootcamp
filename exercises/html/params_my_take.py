import requests
from termcolor import colored
from random import randint

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat"}
)

leg_colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

data = response.json()
print(data)

for joke in data["results"]:
    print(
        f"Dad joke: {colored(joke['joke'], leg_colors[randint(0, len(leg_colors) - 1)])}")
    # this is awful, but I wanted to practice

print("-"*10)
rand_joke = requests.get(url,
                         headers={"Accept": "application/json"}).json()
print(
    f"Random joke: {colored(rand_joke['results'][randint(0, len(rand_joke['results']) - 1)]['joke'], leg_colors[randint(0, len(leg_colors) - 1)])}")

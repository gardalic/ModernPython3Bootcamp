from pyfiglet import figlet_format
from termcolor import colored


def print_art(text, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "red"

    print(colored(figlet_format(text), color=color))


text = input("What do you want to write? ")
color = input("What color? ")

print_art(text, color)

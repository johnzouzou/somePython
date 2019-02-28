import pyfiglet
from termcolor import colored

msg = input("what would you like to print ")
color = input("what color")
colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
if color not in colors:
	color = "white"
art = pyfiglet.figlet_format(msg)
cart = colored(art, color=color)
print(cart)
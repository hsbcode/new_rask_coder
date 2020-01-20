from pyfiglet import figlet_format
from termcolor import colored

message = input("What message do you want to print? ")
colorr = input("What color? ")
figmessage = figlet_format(message).lower()
k = 0
while k == 0:
    try:
        colored_figmessage = colored(figmessage, colorr)
        k = 1
    except KeyError:
        print("Sorry! We don't have that color. Please choose one of these: grey, red, green, yellow, blue, magenta, cyan, white.")
        colorr = input("What color? ").lower()
print(colored_figmessage)

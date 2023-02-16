from pyfiglet import figlet_format


def print_art(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)


msg = input("What would you like to print?\n ")
print_art(msg)

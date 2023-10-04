from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def figlet_text(str, font_name):
    # set the font with code like this, wherein f is the font’s name as a str:
    figlet.setFont(font=font_name)
    return figlet.renderText(str)

def main():
    num_args = len(sys.argv)
    if num_args not in [1,3]:
        print("Invalid usage: You must provide either zero or two arguments.")
        sys.exit(1)

    if num_args == 3:
        if sys.argv[1] not in ["--font", "-f"]:
            print("Invalid usage")
            sys.exit(1)

        font_option = sys.argv[2]

        if font_option not in figlet.getFonts():
            print("Invalid usage: Invalid font")
            sys.exit(1)

    else:
        font_option = random.choice(figlet.getFonts())

    user_input = input("Input: ")
    figletted_text = figlet_text(user_input, font_option)

    print(figletted_text)

if __name__ == "__main__":
    main()

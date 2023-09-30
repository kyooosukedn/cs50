import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Display text in a specific or random font.")

    # Optional argument for specifying the font
    parser.add_argument('-f', '--font', metavar='FONT_NAME', help="Specify the font name")

    # Positional argument for the text
    parser.add_argument('text', nargs='?', default=None, help="Text to be displayed")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(args)

def main():
    names = []

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        if len(names) == 1:
            print(f"Adieu, adieu to {names[0]}")
        elif len(names) == 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}")
        elif len(names) > 1:
            formatted_names = ", ".join(names[:-1]) + f", and {names[-1]}"
            print(f"Adieu, adieu to {formatted_names}")

if __name__ == "__main__":
    main()

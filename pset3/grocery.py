from collections import Counter

def main():
    items = []

    # looping until user inputs control - D
    try:
        while True:
            item = input("")
            items.append(item.upper())
            items_count = Counter(items)

    except EOFError:
        for item, count in items_count.items():
            print("f{count} {item}")


main()

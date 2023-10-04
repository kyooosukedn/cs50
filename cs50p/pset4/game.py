import random
import sys

def is_numeric(value):
    return str(value).isdigit()

def is_valid_level(level):
    return 1 <= level <= 100

def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if is_numeric(user_input):
            return int(user_input)
        else:
            continue

def main():
    while True:
        n = get_numeric_input("Level: ")
        if is_valid_level(n):
            break

    random_integer = random.randint(1, n)
    guess(random_integer)

def guess(random_integer):
    while True:
        guessed_num = get_numeric_input("Guess: ")
        if guessed_num < 0:
            continue
        elif guessed_num < random_integer:
            print("Too small!")
        elif guessed_num > random_integer:
            print("Too large!")
        elif guessed_num == random_integer:
            print("Just right!")
            break

if __name__ == "__main__":
    main()


import random

def main():
    attempt_counter = 0
    incorrect_attempt = 0
    score = 0
    level = get_level()
    while True:
        if attempt_counter == 10:
            break
        try:
            expression = generate_expression(level)
            x, operator, y = parse_expression(expression)
            answer = evaluate_expression(x, operator, y)
            user_answer = int(input(f"{expression} = "))
            if user_answer == answer:
                score += 1
            else:
                incorrect_attempt += 1

                if incorrect_attempt == 3:
                    print(f"Answer = {answer}")
                else:
                    print("EEE")
        except ValueError:
            print("Not a number!")
            break
        attempt_counter += 1

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level (1-3): "))
            if level < 1 or level > 3:
                continue
            else:
                break
        except ValueError:
            continue
    return level

def generate_expression(level):
    x = 0
    y = 0
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    operator = "+"
    return f"{x} {operator} {y}"

def parse_expression(expression):
    x, operator, y = expression.split()
    return int(x), operator, int(y)

def evaluate_expression(x, operator, y):
    return x + y

if __name__ == "__main__":
    main()


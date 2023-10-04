import os

def interpret(expression):

    x, y, z = expression.split(" ")

    x = int(x)
    z = int(z)

    if y == "+":
        res = x + z
    elif y == "-":
        res = x - z
    elif y == "*":
        res = x * z
    elif y == "/":
        if z == 0:
            return "Division by zero is not allowed."
        else:
            res = x / z

    return float(res)

def main():
    expression = input("Expression: ")
    print(interpret(expression))

main()
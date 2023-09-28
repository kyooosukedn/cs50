def main():
    camel_case_input = input("camelCase: ")
    snake_case_output = ""

    for c in camel_case_input  :
        if c.isupper():
            snake_case_output += "_"
            c = c.lower()
        snake_case_output += c

    print("snake_case: " + snake_case_output)

if __name__ ==  "__main__":
    main()

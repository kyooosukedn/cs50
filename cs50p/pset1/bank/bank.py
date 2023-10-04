def main():
    user_input = input("Greeting: ")

    if user_input.lower() == "hello":
        print("$0")
    elif user_input.lower().startswith("h") :
        print("$20")
    else:
        print("$100")

main()

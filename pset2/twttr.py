def is_vowel(character):
    if character.lower() in ("a", "i", "u", "e", "o"):
        return True
    else:
        return False

def main():
    user_input = input("Input: ")
    output = ""
    for i in user_input:
        if is_vowel(i) == True:
            continue
        output += i
    print("Output: " + output)


if __name__ == "__main__":
    main()

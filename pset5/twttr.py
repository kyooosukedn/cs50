def is_vowel(character):
    if character.lower() in ("a", "i", "u", "e", "o"):
        return True
    else:
        return False

def shorten(s):
    output = ""
    for i in s:
        if is_vowel(i) == True:
            continue
        output += i

    return output

def main():
    user_input = input("Input: ")
    output = shorten(user_input)
    print("Output: " + output)

if __name__ == "__main__":
    main()

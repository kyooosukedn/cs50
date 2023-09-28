def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    '''
“All vanity plates must start with at least two letters.” // 1
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” // 2
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
vanity plate; AAA22A would not be acceptable. // 3
The first number used cannot be a ‘0’.” // 4
“No periods, spaces, or punctuation marks are allowed.” // 5
    '''
    # Plates must start with at least two letters
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # Plates may contain a maxi of 6 chars and min of 2 chars
    if len(s) < 2 or len(s) > 6:
        return False

    # If numbers is not at the end of the sequence chars
    if not s[-1].isdigit():
        return False

    # First number cant be zero
    for char in s:
        if char.isdigit():
            if int(char) == 0:
                return False
            else:
                break

    # No periods, spaces, or punctuation marks
    if any(char in s for char in "., !"):
        return False

    return True


main()


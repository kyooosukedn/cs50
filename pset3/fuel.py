def main():
    while(True):
        try:
            fraction = input("Fraction: ").split("/")

            if len(fraction) != 2:
                raise ValueError

            x = int(fraction[0])
            y = int(fraction[1])

            if y == 0:
                raise ZeroDivisionError

            if x > y:
                raise ValueError

            percentage = (x / y * 100)

            if percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            else:
                print(round(percentage),"%")
                break
        except ValueError:
            print("Invalid Input. Please enter the fraction again: ")
        except ZeroDivisionError:
            print("Zero division error: The denominator cannot be zero")

main()


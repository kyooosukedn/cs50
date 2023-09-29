from datetime import datetime

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

def get_valid_date():
    while True:
        user_input = input("Enter the date: ")
        try:
            # Try to parse the date with both formats
            date = datetime.strptime(user_input, "%m/%d/%Y")
        except ValueError:
            try:
                date = datetime.strptime(user_input, "%B %d, %Y")
            except ValueError:
                print("Invalid input date. Try again with month-date-year or Month date, year format")
                continue

        # Check if month or day is valid
        if date.month not in range(1, 13) or date.day not in range(1,32):
            print("Invalid date. Please enter the correct date")

        return date

def main():
    date = get_valid_date()
    formatted_date = date.strftime("%Y-%m-%d")
    print(formatted_date)

if __name__ == "__main__":
    main()

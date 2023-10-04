def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    # Breakfast time : 7 till 8
    # Lunch time : 12 till 13
    # Dinner time : 18 till 19

    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + (int(minutes) / 60)

if __name__ ==  "__main__":
    main()
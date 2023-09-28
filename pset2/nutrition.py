def main():
    item = input("Item: ")
    calories = check_nutrition(item)
    print("Calories: " + str(calories))

def check_nutrition(item):
    # Dictionary to map fruits and cals
    fruits = {
        "apple"  : 130,
        "avocado": 50,
        "banana" : 110,
        "cantaloupe"  : 50,
        "grapefruit"  : 60,
        "grapes"  : 90,
        "honeydrew melon"  : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80
    }
    if item in fruits:
        calories = fruits.get(item.lower(), "")
        return calories

main()


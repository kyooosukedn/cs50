def main():
    change_owed = 50
    amount_due = 50
    inserted_coin = 0

    while(change_owed != 0):
        amount_due -= inserted_coin
        print("Amount due: " + str(amount_due))
        inserted_coin = int(input("Insert coin: "))
        change_owed -= inserted_coin
        print("Change owed: " + str(change_owed))

if __name__ ==  "__main__":
    main()

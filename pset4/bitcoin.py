import requests
import sys

def main():
    try:
        # Check if argument exists
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)

        bitcoins = float(sys.argv[1])

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()

        # parse in json
        data = response.json()
        usd_price = data["bpi"]["USD"]["rate_float"]

        total_price = bitcoins * usd_price

        print(f"${total_price:,.4f}")

    except requests.RequestException as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print("Command line argument is not a number")
        sys.exit(1)
    except KeyError as e:
        sys.exit(1)

if __name__ == "__main__":
    main()

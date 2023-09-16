def convert(str):

    # Define a dictionary for emojis :) and :(
    emoticon_to_emoji = {
            ':)' : '🙂',
            ':(' : '🙁'
    }

    for emoticon, emoji in emoticon_to_emoji.items() :
        str = str.replace(emoticon, emoji)

    return str

def main():
    userInput = input("")
    print(convert(userInput))

main()

'''
# Another solution
def main():
    userInput = input("")
    print(convert(userInput))

def convert(str):
    return str.replace(':)', '🙂').replace(':(', '🙁')

main() 
'''
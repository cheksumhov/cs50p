# Function to onvert emoticons to emoji
def convert(input):
    if ":)" or ":(" in input:
        return input.replace(":)", "🙂").replace(":(", "🙁")

# Main asks the user for input and then caslls the convert function to replace colons with emoji
def main():
    usertext = convert(input("Enter a word and emoticon: "))
    print(usertext)

main()

from hangman import hangman

realWord = input("Enter the word you would like the person to guess: ")

def drawLine(): 
    for letter in realWord:
        print()
        print("-", end="")
    # Prints new line so terminal doesn't get squished next to it
    print()


def main():
    drawLine()

if __name__ == "__main__":
    main()
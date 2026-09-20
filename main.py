from hangman import hangman

# Draws line for letters
def drawLine(realWord): 
    print()
    for letter in realWord:
        print("-", end="")
    # Prints new line so terminal doesn't get squished next to it
    print()

# Empty list declerations
word = []
wordLetters = []
guessedLetters = []

# Global game state decleration
letterHasBeenGuessed = False

def init():
    print("===============================")
    print("      Hangman for JeyGazos     ")
    print("===============================")
    print()

    print("See INSTRUCTIONS.md for Game Instructions")
    print()

    realWord = input("Enter the word you would like the other person to guess: ")

    drawLine(realWord)
    word.append(realWord)
    for letter in realWord:
        wordLetters.append(letter)

    return realWord

def main():
    init()

    global letterHasBeenGuessed

    while letterHasBeenGuessed == False:
        guessChoice = input("Guess a letter or word? (Letter/Word): ")

        # Letter Selected
        if (guessChoice == "Letter"):
            guessedLetter = input("Guess a letter: ")
            guessedLetters.append(guessedLetter)
            if guessedLetter in wordLetters:
                print("Correct!")
                print(f"Guessed Letters: {guessedLetters}")
            elif guessedLetter in guessedLetters:
                print("You already guessed that letter!")
                print(f"Guessed Letters: {guessedLetters}")
            else:
                print("Incorrect!")
                print(f"Guessed Letters: {guessedLetters}")
        # Word Selected
        elif (guessChoice == "Word"):
            guessedWord = input("Guess the word: ")
            if guessedWord in word:
                print("You have guessed the correct word! Congrats!")
                letterHasBeenGuessed = True
            else:
                print("You have not guessed the right word")
        # Catch-all statement
        else:
            print("Please enter a valid operation")

if __name__ == "__main__":
    main()
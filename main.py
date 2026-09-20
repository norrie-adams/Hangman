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

# Global Variables
gameOver = False
hangmanPhase = 0
realWord = ""

def init():
    global realWord
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

def main():
    init()

    global gameOver
    global hangmanPhase
    global realWord

    while gameOver == False:
        guessChoice = input("Guess a letter or word? (Letter/Word): ")

        # Letter Selected
        if (guessChoice == "Letter"):
            guessedLetter = input("Guess a letter: ")
            if guessedLetter in wordLetters:
                print("Correct!")
                guessedLetters.append(guessedLetter)
                print(f"Guessed Letters: {guessedLetters}")
            elif guessedLetter in guessedLetters:
                print("You already guessed that letter!")
                print(f"Guessed Letters: {guessedLetters}")
            else:
                print("Incorrect!")
                guessedLetters.append(guessedLetter)
                print(hangman[hangmanPhase])
                hangmanPhase += 1
                print(f"Guessed Letters: {guessedLetters}")
        # Word Selected
        elif (guessChoice == "Word"):
            guessedWord = input("Guess the word: ")
            if guessedWord in word:
                print("You have guessed the correct word! Congrats!")
                gameOver = True
            else:
                print("You have not guessed the right word")
        # Catch-all statement
        else:
            print("Please enter a valid operation")

        # Checks if game is over
        if (hangmanPhase == 6):
            print("You have lost!")
            print(f"The word was: {realWord}")
            print(hangman[hangmanPhase])
            gameOver = True

if __name__ == "__main__":
    main()
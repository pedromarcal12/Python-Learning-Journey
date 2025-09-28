# Creating the game Hangman based on "The Self-Taught Programmer"

# Method to create the game
from ast import Break


def hangman(word) :
    # Variable for keeping track of wrong guesses
    wrong = 0
    # Variable for creating our Hangman
    stages = [ 
             "",
             "________",
             "|                 ",
             "|         |       ",
             "|         0       ",
             "|        /|\      ",
             "|        / \      ",
             "|                 "
             ]

    # Creating a list to store each character in the variable word     
    letters = list(word)
    # Creating a variable to populate the board with an underscore for every character
    board = ["__"] * len(word)
    # Boolean to check every time if the player is a winner
    win = False
    print("Welcome to the game")

    # While loop that will keep going until the player guesses more wrong letters than the number of string that make the Hangman
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess one letter : "
        char = input(msg)
        if char in letters:
            cind = letters.index(char)
            board[cind] = char
            letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Winner!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! The word was {}.".format(word))


hangman("cat")
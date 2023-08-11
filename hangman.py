

import random
import cowsay
import pandas as pd
import tkinter
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init
init(autoreset=True)




#Im looking to make a function where the player can add new words to a forth sheet and it saves in listas.xlsx

#And finally try and use pyscript



def main():
    font = Figlet(font = "colossal")
    print()
    print(font.renderText("Hangman"))
    print("¡¡Welcome to Hangman.py!!")
    print("¿Which word topic would you like to try?")
    print()

    while True:
        try:
            
            print("1.- Soccer Players")
            print("2.- Movie Names")
            print("3.- Videogame Names")
            print("4.- Random topic")
            choice = int(input(Fore.BLUE + "Choose an option: "))
            break
        except ValueError:
            print(Fore.RED + "Choose 1 to 3 to select category and any other number for random")
            pass

    word = secretWord(choice)
    blank = spaces(word)
    
    print()
    print(blank)
    hangman(word,blank)
    
























#--------------------------------------FUNCTIONS TO MAKE THE GAME TO WORK PROPERLY --------------------------------------





#Function that creates the blank spaces
def spaces(word):    
    blank = str("")
    for letter in word:
        if letter == " ":
            blank += " "
        elif letter.isnumeric() == True:
            blank +=letter
        else:
            blank += "_"

    return str(blank)





#Function which reads the excel file and depending on the players choice, returns a random word of themes Soccer, Videogames or Movies
def secretWord(selection):
    #Reads the excel file
    path_excel = "listas.xlsx"
    #Reads and separates each worksheet
    paginaFutbol = pd.read_excel(path_excel,sheet_name= 'Futbol' )
    paginaVideojuegos = pd.read_excel(path_excel,sheet_name= 'VideoJuegos' )
    paginaPeliculas = pd.read_excel(path_excel,sheet_name= 'Peliculas' )
    #Conditional for when the player wants to get a random word from the three themes
    

    if selection not in [1,2,3]:
        selection = random.randint(1,3)
    if selection == 1:
        columna_nombre = paginaFutbol["Nombre"].to_list()
    elif selection == 2:
        columna_nombre = paginaPeliculas["Nombre"].to_list()
    elif selection == 3:
        columna_nombre = paginaVideojuegos["Nombre"].to_list()
#Selects the random word/phrase
    secretWord = random.choice(columna_nombre)
    return str(secretWord).lower()


def hangman(word,blank):
    hangman = {
    0: '''
        ------
        |    |
        |     
        |    
        |    
        |    
        ---
            ''',
    1: '''
        ------
        |    |
        |    O
        |    
        |    
        |    
        ---
    ''',
    2: '''

        ------
        |    |
        |    O
        |    |
        |    
        |    
        ---
    ''',

    3: '''
        ------
        |    |
        |    O
        |   /|
        |    
        |    
        ---
    ''',

    4: '''
        ------
        |    |
        |    O
        |   /|/
        |    
        |    
        ---
    ''',
    5:'''
        ------
        |    |
        |    O
        |   /|/
        |   / 
        |    
        ---

    ''',
    6:'''
        ------
        |    |
        |    O
        |   /|/
        |   / /
        |    
        ---

    '''

    }

    word_list = list(word)
    blank_list = list(blank)
    usedLetters = []

# Number of attempts made by the player.
    attempts = int(0)

    # Main game loop.
    while True:
        try:
            # Check if the player still has attempts left (maximum attempts = 6, since there are 7 hangman drawings).
            if attempts == 6:
                print("GAME OVER")
                print("The word was: ", end="")
                print(*word_list)
                break
            if "_" not in blank_list:
                print("¡Ya ganaste!")
                break
            # Display the list of used letters and the number of attempts remaining.
            print("Used letters:", *usedLetters, sep= "")
            print("Attempts left:", 6 - attempts)

            # Ask the player to input a letter.
            guess = input("Select a letter: ").lower()

            # Check if the guessed letter is in the word.
            if guess in usedLetters:
                # If the guessed letter was already used, prompt the player to try another letter.
                print("You already used that letter, try another one.")
                #Check if the guess is equal to the secret word
            elif guess == word:
                print("Ya ganaste")
                break
            else:
                usedLetters.append(guess)
                if guess in word_list:
                    # If the guessed letter is correct, update the corresponding blank list.
                    for i in range(len(word)):
                        if guess == word[i]:
                            blank_list[i] = guess
                else:
                    # If the guessed letter is wrong, increment the attempts count.
                    attempts += 1
            # Display the current state of the word to guess (with correctly guessed letters) and the hangman drawing.
            print("-----------------------------------------", attempts ,"------------------------------------------------")
            print(*blank_list)
            print()
            print(hangman[attempts])
        except ValueError:
            # Handle the case when the player inputs a non-letter character.
            print("Solo letras")
            pass

if __name__ == "__main__":
    main()


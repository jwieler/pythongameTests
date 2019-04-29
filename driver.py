#!/usr/bin/python3
import hangman
import wordTyper
import battleship

game = 0

while(game == 0):
    print("What game would you like to play?")
    print("1. Hangman")
    print("2. Word Typer")
    print("3. Battleship")
    print("4. Exit Program.")
    game = input()

    if(game == '1'):
        hangman.main()
        game = 0
    elif(game == '2'):
        wordTyper.main()
        game = 0
    elif(game == '3'):
        battleship.main()
        game = 0
    elif(game == '4'):
        break
    else:
        game = 0

#!/usr/bin/python3

# Author: Jacob Wieler
# Date: 2018/03/30
# Title: Basic Hangman

#library for hidden user input entry
import getpass

#function definitions
def validName(name):
	if name.isspace():
		return False
	elif  name.isdigit():
		print("Sorry, name cannot contain numbers.")
		return False
	elif name == "":
		print("Sorry, name cannot be empty.")
		return False
#	elif name.isalpha()
	else:
		return True

def validWord(word):
	for i in range(0, len(word)):
		if word[i] == ' ':
			return False
		elif word[i].isdigit():
			return False
	return True

def validGuess(guess, guessedLetters):
	if len(guess) > 1:
		print("Sorry, guesses can only be 1 character long.")
		return False
	elif guess.isdigit():
		print("Sorry, numbers are not allowed in the guess.")
		return False
	elif guess.isspace():
		return False
	else:
		for i in range(0, len(guessedLetters)):
			if guessedLetters[i] == guess:
				return False
		if guess.isalpha():
			return True

def printBoard(wordLetters, guessedLetters):
	foundLetter = False

	for i in range (0, len(wordLetters)):
		for j in range(0, len(guessedLetters)):
			if wordLetters[i].lower() == guessedLetters[j].lower():
				print(" " + wordLetters[i].upper() + " ", end = "")
				foundLetter = True
		if not foundLetter:
			print(" _ ", end = "")
		foundLetter = False
	print("\n")

def checkWin(wordLetters, guessedLetters):
	totalRight = 0

	for i in range(0 , len(wordLetters)):
		for j in range(0 , len(guessedLetters)):
			if wordLetters[i].lower() == guessedLetters[j].lower():
				totalRight += 1

	if totalRight == len(wordLetters):
		return True
	else:
		return False

def playAgain(replay):
	for i in replay:
		if i.lower() == 'y':
			return True
	return False

def main():
	#main
	#variable declarations and initializations
	#user names
	name1 = " "
	name2 = " "

	#controls replay of game
	replay = "yes"

	#scores of players 1 and 2
	score1 = 0
	score2 = 0

	while(not validName(name1)):
		name1 = input("What is player one's name? ")

	while(not validName(name2)):
		name2 = input("What is player two's name? ")

	while(playAgain(replay)):
		#word to hold entered word to guess
		word = " "
		#holds user's guess (single char)
		guess = " "

		#lists of letters in word and guessed letters
		guessedLetters = []
		wordLetters = []

		bool = True

		while(not validWord(word)):
			print(name1 + ", enter a word for", name2, "to guess.")
			word = getpass.getpass("")

		#	if not validName(word):
		#		bool = False

		for i in word:
			wordLetters += i

		bool = True

		#for i in range(101):
		#	print("*")

		while(bool):
			printBoard(wordLetters, guessedLetters)

			if len(guessedLetters) > 0:
				print(name2 + "\'s guessed letters:", guessedLetters)

			while(not validGuess(guess, guessedLetters)):
				print("Guess a letter,", name2 + ": ", end = "")
				guess = input()
			guessedLetters += guess


			if checkWin(wordLetters, guessedLetters):
				bool = False
				printBoard(wordLetters, guessedLetters)
				print("Congrats,", name2 + ", you've guessed", name1 + "\'s word!")
				score2 += 1

		print(name1 + "\'s score:", score1)
		print(name2 + "\'s score:", score2)
		print("Play again?")
		replay = input()

		#
		#	if guess.lower() == word.lower():
		#		print("Congrats,", name2, "you found the word!!")
		#		score2 += 1
		#		bool = False
		#	else:
		#		print(name2 + ", what an idiot, you're so wrong dude, guess again")
		#		guess  = " "

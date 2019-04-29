#!/usr/bin/python3

# Author: Jacob Wieler
# Date: 2019/01/02
# Title: Basic Word Typer

import random
import time

wordList = ("The birch canoe slid on the smooth planks~Glue the sheet to the dark blue background~It's easy to tell the depth of a well~These days a chicken leg is a rare dish~Rice is often served in round bowls").split("~")
timeBefore = 0.0
timeAfter  = 0.0
totalTime = 0
words = []
game = 'y'
typedWord = ""


def playAgain(replay):
	for i in replay:
		if i.lower() == 'y':
			return True
	return False

def checkRecord():
    currentRecord = 0
    try:
        f = open("wordTyperRecord.txt", "r")
        currentRecord = f.read()
        if(len(currentRecord) < 1):
                record = 0
                print("No record exists yet!")
        else:
                currentRecordList = currentRecord.split(":")
                currentRecordNum = float(currentRecordList[0])
                currentRecordHolder = currentRecordList[1]
                print("Current record:", str(currentRecordNum) + " WPM by:", currentRecordHolder)
    except FileNotFoundError:
        f = open("wordTyperRecord.txt", "w")
        f.close()
        print("No record exists yet!")

def main():
    game = 'y'

    while(playAgain(game)):
        num = random.randint(0, 4)
        words = wordList[num].split(" ")
        print(words)
        print("These are the words that you will need to type.")

        ready = 'n'
        while(not playAgain(ready)):
            print("y: Play\nr: Check record")
            ready = input(":")
            if(ready == 'r'):
                checkRecord()
        timeBefore = int(round(time.time()))
        right = 0
        wrong = 0
        for i in words:
            print(i)
            typedWord = input(":")
            if(typedWord == i):
                print("Correct!\n\n\n\n")
                right += 1
            else:
                print("Wrong!\n\n\n\n")
                wrong += 1

        timeAfter = int(round(time.time()))
        totalTime = (timeAfter - timeBefore)
        print("It took you ", totalTime, "seconds!")
        print("You got ", str(right) + "/" + str(wrong + right), "words right ("  + str(right / (wrong + right) * 100) + "%)")
        print("Your typing speed is: ", str((right / totalTime) * 60), "WPM")

        currentRecord = 0
        try:
            f = open("wordTyperRecord.txt", "r")
            currentRecord = f.read()
        except FileNotFoundError:
            f = open("wordTyperRecord.txt", "w")
            f.close()

        currentRecordNum = 0
        if(len(currentRecord) < 1):
            record = 0
        else:
            currentRecordList = currentRecord.split(":")
            currentRecordNum = float(currentRecordList[0])
            currentRecordHolder = currentRecordList[1]

        f.close()

        if(((right / totalTime) * 60) > currentRecordNum):
            f = open("wordTyperRecord.txt", "w")
            print("Congrats you set the record for WPM! Enter your name!")
            name = input(":")
            f.write(str((right / totalTime) * 60) + ":" + name)
        print("Would you like to play again?")
        game = input(":")

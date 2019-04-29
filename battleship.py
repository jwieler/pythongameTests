#!/usr/bin/python3

# Author: Jacob Wieler
# Date: 2019/01/03
# Title: Basic Battleship

#battleship board is 10x10 (A-J top, 1-10 right)

class SmallestShip:
    length = 2
    placed = False
    body = None
    position = None

class ThreeLongShip:
    length = 3
    placed = False
    body = None
    position = None

class FourLongShip:
    length = 4
    placed = False
    body = None
    position = None

class Battleship:
    length = 6
    placed = False
    body = None
    position = None

def printBoard(position):
    print("  A  B  C  D  E  F  G  H  I  J")

    if(position[0].upper() == 'A'):
        x = 0
    elif(position[0].upper() == 'B'):
        x = 1
    elif(position[0].upper() == 'C'):
        x = 2
    elif(position[0].upper() == 'D'):
        x = 3
    elif(position[0].upper() == 'E'):
        x = 4
    elif(position[0].upper() == 'F'):
        x = 5
    elif(position[0].upper() == 'G'):
        x = 6
    elif(position[0].upper() == 'H'):
        x = 7
    elif(position[0].upper() == 'I'):
        x = 8
    elif(position[0].upper() == 'J'):
        x = 9

    y = int(position[1])

    init = False
    for j in range(10):
        if(init):
            print("")
        print(j, end="")
        init = True
        for i in range(10):
            if(j == y and i == x):
                print("[x]", end="")
            else:
                print("[~]", end="")
    print("")


def printBoard2(board):
    print("  A  B  C  D  E  F  G  H  I  J")

    init = False
    for j in range(10):
        if(init):
            print("")
        print(j, end="")
        init = True
        for i in range(10):
            if(board[i][j] == 1):
                print("[o]", end="")
            else:
                print("[~]", end="")
    print("")

def validPosition(position):
    validAlpha = list("ABCDEFEGHIJ")
    validNum = list("0123456789")

    if(len(position) != 2):
        return False
    elif(not position[0].upper() in validAlpha):
        return False
    elif(not position[1] in validNum):
        return False
    else:
        return True

def validPlacement(start, end, ship, board):
    if(start[0] == end[0]):
        x = convertCharToNum(start[0])
        startNum = int(start[1])
        endNum = int(end[1])
        if(startNum > endNum):
            while(startNum != endNum - 1):
                y = startNum
                if(board[x][y] == 1):
                    return False
                startNum -= 1
        elif(startNum < endNum):
            while(startNum != endNum + 1):
                y = startNum
                if(board[x][y] == 1):
                    return False
                startNum += 1
    if(int(end[1]) - int(start[1]) == ship.length - 1 and start[0] == end[0]):
        return True
    elif(int(start[1]) - int(end[1]) == ship.length - 1 and start[0] == end[0]):
        return True
    elif(start[1] == end[1] and convertCharToNum(start[0]) - convertCharToNum(end[0]) == ship.length - 1):
        return True
    elif(start[1] == end[1] and convertCharToNum(end[0]) - convertCharToNum(start[0]) == ship.length - 1):
        return True
    else:
        return False

def convertCharToNum(character):
    if(character.upper() == 'A'):
        return 0
    elif(character.upper() == 'B'):
        return 1
    elif(character.upper() == 'C'):
        return 2
    elif(character.upper() == 'D'):
        return 3
    elif(character.upper() == 'E'):
        return 4
    elif(character.upper() == 'F'):
        return 5
    elif(character.upper() == 'G'):
        return 6
    elif(character.upper() == 'H'):
        return 7
    elif(character.upper() == 'I'):
        return 8
    elif(character.upper() == 'J'):
        return 9
    else:
        return -1

def changeBoard(start, end, ship, board):
    startList = list(start)
    endList = list(end)

    if(start[0] == end[0]):
        x = convertCharToNum(start[0])
        startNum = int(start[1])
        endNum = int(end[1])
        if(startNum > endNum):
            while(startNum != endNum - 1):
                print(startNum)
                y = startNum
                board[x][y] = 1
                startNum -= 1
        elif(startNum < endNum):
            while(startNum != endNum + 1):
                print(startNum)
                y = startNum
                board[x][y] = 1
                startNum += 1
    elif(start[1] == end[1]):
        y = int(start[1])
        startNum = convertCharToNum(start[0])
        endNum = convertCharToNum(end[0])
        if(startNum > endNum):
            while(startNum != endNum - 1):
                print(startNum)
                x = startNum
                board[x][y] = 1
                startNum -= 1
        elif(startNum < endNum):
            while(startNum != endNum + 1):
                print(startNum)
                x = startNum
                board[x][y] = 1
                startNum += 1
    return board

def main():
    position = ["",""]

    #printBoard(position)

    playerBoard = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

    small1 = SmallestShip()
    small2 = SmallestShip()
    small3 = SmallestShip()
    small4 = SmallestShip()

    small1.position = ["", ""]
    small2.position = ["", ""]
    small3.position = ["", ""]
    small4.position = ["", ""]

    small1.body = [False, False]
    small2.body = [False, False]
    small3.body = [False, False]
    small4.body = [False, False]

    threeLong1 = ThreeLongShip()
    threeLong2 = ThreeLongShip()
    threeLong3 = ThreeLongShip()

    threeLong1.position = ["", ""]
    threeLong2.position = ["", ""]
    threeLong3.position = ["", ""]

    threeLong1.body = [False, False, False]
    threeLong2.body = [False, False, False]
    threeLong3.body = [False, False, False]

    fourLong1 = FourLongShip()
    fourLong2 = FourLongShip()

    fourLong1.position = ["", ""]
    fourLong2.position = ["", ""]

    fourLong1.body = [False, False, False, False]
    fourLong2.body = [False, False, False, False]

    battleship = Battleship()

    battleship.position = ["", ""]

    battleship.body = [False, False, False, False, False, False]

    printBoard2(playerBoard)

    print("Place boat 1 somewhere (Boat 1: oo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, small1, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    small1.position = [start, end]
    playerBoard = changeBoard(start, end, small1, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 2 somewhere (Boat 2: oo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, small2, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    small2.position = [start, end]
    playerBoard = changeBoard(start, end, small2, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 3 somewhere (Boat 3: oo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, small3, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    small3.position = [start, end]
    playerBoard = changeBoard(start, end, small3, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 4 somewhere (Boat 4: oo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, small4, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    small4.position = [start, end]
    playerBoard = changeBoard(start, end, small4, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 5 somewhere (Boat 5: ooo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, threeLong1, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    threeLong1.position = [start, end]
    playerBoard = changeBoard(start, end, threeLong1, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 5 somewhere (Boat 6: ooo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, threeLong1, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    threeLong2.position = [start, end]
    playerBoard = changeBoard(start, end, threeLong2, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 7 somewhere (Boat 7: ooo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, threeLong3, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    threeLong3.position = [start, end]
    playerBoard = changeBoard(start, end, threeLong3, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 8 somewhere (Boat 8: oooo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, fourLong1, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    fourLong1.position = [start, end]
    playerBoard = changeBoard(start, end, fourLong1, playerBoard)
    printBoard2(playerBoard)

    print("Place boat 9 somewhere (Boat 9: oooo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, fourLong2, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    fourLong2.position = [start, end]
    playerBoard = changeBoard(start, end, fourLong2, playerBoard)
    printBoard2(playerBoard)

    print("Place your battleship somewhere (Battleship: oooooo).")
    start = ""
    end = ""
    startList = ["0", "0"]
    endList = ["0", "0"]
    while(not validPlacement(startList, endList, battleship, playerBoard)):
        startList = ["0", "0"]
        endList = ["0", "0"]
        while(not validPosition(startList)):
            print("From (A0 - J9): ", end="")
            start = input()
            startList = list(start)
        while(not validPosition(endList)):
            print("To (A0 - J9): ", end="")
            end = input()
            endList = list(end)

    battleship.position = [start, end]
    playerBoard = changeBoard(start, end, battleship, playerBoard)
    printBoard2(playerBoard)

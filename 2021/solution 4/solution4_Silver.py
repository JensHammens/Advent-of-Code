from ctypes import resize
import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input = open(os.path.join(location,'solutiondata')).read()
lines = input.split("\n")

bingoNumbers = [72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5]
board = []
boards = []

def checkiswin(tempBoard,colindex,rowindex):
    if(tempBoard[rowindex][0][1]==True and tempBoard[rowindex][1][1]==True and tempBoard[rowindex][2][1]==True and tempBoard[rowindex][3][1]==True and tempBoard[rowindex][4][1]==True):
        return True
    if(tempBoard[0][colindex][1]==True and tempBoard[1][colindex][1]==True and tempBoard[2][colindex][1]==True and tempBoard[3][colindex][1]==True and tempBoard[4][colindex][1]==True):
        return True
    return False

def calculatescore(tempBoard,lastnum):
    sum=0
    for row in tempBoard:
        for col in row:
            if(col[1]==False):
                sum+=col[0]
    return sum*lastnum

for line in lines:
    if(line==""):
        boards.append(board)
        board = []
        continue
    numbers = line.replace("  "," ").strip().split(" ")
    numwithset = []
    for number in numbers:
        numwithset.append([int(number),False])
    board.append(numwithset)

def getfirstwinner():
    for number in bingoNumbers:
        for board in boards:
            for (rowindex,row) in enumerate(board):
                for (colindex,col) in enumerate(row):
                    if(col[0]==number):
                        col[1]=True
                        if(checkiswin(board,colindex,rowindex)==True):
                            return calculatescore(board,number)

print(getfirstwinner())
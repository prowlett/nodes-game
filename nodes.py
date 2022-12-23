# config

boardsize = 3

# code

from math import ceil

def score(position):
    if "N"*ceil(boardsize/2) in position:
        return 1
    elif "P"*ceil(boardsize/2) in position:
        return -1
    else:
        return 0

def minimax(position,turn):
    thisscore = score(position)
    if "." in position and thisscore==0:
        scores = []
        for i in range(boardsize):
            if position[i]==".":
                scores.append(minimax(position[0:i]+turn+position[i+1:boardsize],"N" if turn == "P" else "P"))
        if turn=="N":
            thisscore = max(scores)
        else:
            thisscore = min(scores)
        if board == position:
            return thisscore,scores.index(thisscore)
        else:
            return thisscore
    else:
        return thisscore

board = "."*boardsize
outcome,move = minimax(board,"N")
if outcome == 1:
    print("Win for next player in position {}".format(move))
elif outcome == -1:
    print("Win for previous player in position {}".format(move))
else:
    print("Draw")


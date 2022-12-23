# config

boardsize = 3

# code

from math import ceil

c=0

def score(position):
    global c
    c= c+1
    if "N"*ceil(boardsize/2) in position:
        return 1
    elif "P"*ceil(boardsize/2) in position:
        return -1
    else:
        return 0

def minimax(position,turn):
    thisscore = score(position)
    if "." in position and thisscore==0:
        children_output = ""
        scores = []
        for i in range(boardsize):
            if position[i]==".":
                pos_to_try = position[0:i]+turn+position[i+1:boardsize]
                thisoutscore,thisposition = minimax(pos_to_try,"N" if turn == "P" else "P")
                scores.append(thisoutscore)
                children_output = "{} [{}]".format(children_output,thisposition)
        
        if turn=="N":
            thisscore = max(scores)
        else:
            thisscore = min(scores)
        thisi = scores.index(thisscore)
        children_output = "{} {} {}".format(position,thisscore,children_output)
        if position == "."*boardsize:
            return thisscore,children_output,thisi
        else:
            return thisscore,children_output
    else:
        return thisscore,"{} {}".format(position,thisscore)

board = "."*boardsize
outcome,position,move = minimax(board,"N")
if outcome == 1:
    print("Win for next player in position {}".format(move))
elif outcome == -1:
    print("Win for previous player in position {}".format(move))
else:
    print("Draw")
print("searched {} positions".format(c))

latexoutput1 = """
\\documentclass{standalone}
\\usepackage{forest}
\\begin{document}
    \\begin{forest}
        ["""
latexoutput2 = """] 
    \\end{forest}
\\end{document}
"""
f = open("nodes-{}-game-tree.tex".format(boardsize),"w")
f.write("{}{}{}".format(latexoutput1,position,latexoutput2))
f.close()


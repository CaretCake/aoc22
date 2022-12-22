file = open("input.txt", "r")


# Rock: 1 pt
#   A, X
# Paper: 2 pt
#   B, Y
# Scissors: 3 pt
#   C, Z


scores = {
    "A X": 4, #rock, rock - draw 3
    "A Y": 8, #rock, paper - win 6
    "A Z": 3, #rock, scissors - loss 0
    "B X": 1, #paper, rock - loss 0
    "B Y": 5, #paper, paper - draw 3
    "B Z": 9, #paper, scissors - win 6
    "C X": 7, #scissors, rock - win 6
    "C Y": 2, #scissors, paper - loss 0
    "C Z": 6  #scissors, scissors - draw 3
}


score = 0

for line in file:
    score += scores[' '.join(line.split())]

print(score)

file.close()
file = open("input.txt", "r")


# Rock: 1 pt
#   A, X
# Paper: 2 pt
#   B, Y
# Scissors: 3 pt
#   C, Z

# Part two logic:
# Rock: 1 pt
#   A
# Paper: 2 pt
#   B
# Scissors: 3 pt
#   C
# X - need loss
# Y - need draw
# z - need win

scores = {
    "A X": 3, #rock - loss 0, scissors 3
    "A Y": 4, #rock - draw 3, rock, 1
    "A Z": 8, #rock - win 6, paper 2
    "B X": 1, #paper - loss 0, rock 1
    "B Y": 5, #paper - draw 3, paper 2
    "B Z": 9, #paper - win 6, scissors 3
    "C X": 2, #scissors - loss 0, paper 2
    "C Y": 6, #scissors - draw 3, scissors 3
    "C Z": 7  #scissors - win 6, rock 1
}


score = 0

for line in file:
    score += scores[' '.join(line.split())]

print(score)

file.close()
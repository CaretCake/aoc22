# input:
# #-#,#-#

file = open("input.txt", "r")

totalOverlapCount = 0

for line in file:
    assignments = ' '.join(line.split()).split(',')
    assignmentOne = assignments[0].split('-')
    assignmentTwo = assignments[1].split('-')
    if ((int(assignmentOne[0]) >= int(assignmentTwo[0]) and int(assignmentOne[0]) <= int(assignmentTwo[1])) or
        (int(assignmentOne[1]) >= int(assignmentTwo[0]) and int(assignmentOne[1]) <= int(assignmentTwo[1])) or
        (int(assignmentTwo[0]) >= int(assignmentOne[0]) and int(assignmentTwo[0]) <= int(assignmentOne[1])) or
        (int(assignmentTwo[0]) >= int(assignmentOne[0]) and int(assignmentTwo[0]) <= int(assignmentOne[1]))):
        totalOverlapCount += 1

print(totalOverlapCount)

file.close()
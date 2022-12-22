# input:
# #-#,#-#

file = open("input.txt", "r")

totalOverlapCount = 0

for line in file:
    assignments = ' '.join(line.split()).split(',')
    assignmentOne = assignments[0].split('-')
    assignmentTwo = assignments[1].split('-')
    if int(assignmentOne[0]) >= int(assignmentTwo[0]) and int(assignmentOne[1]) <= int(assignmentTwo[1]):
        totalOverlapCount += 1
    elif int(assignmentOne[0]) <= int(assignmentTwo[0]) and int(assignmentOne[1]) >= int(assignmentTwo[1]):
        totalOverlapCount += 1

print(totalOverlapCount)

file.close()
import time
def main():
    file = open("input.txt", "r")
    left = 0
    right = 1
    for line in file:
        while right < len(line):
            if right < 4:
                right += 1
                continue
            potentialMarker = line[left:right]
            markerSet = set(potentialMarker)
            if len(markerSet) == 4:
                print(f"{potentialMarker} : {right}")
                break
            left += 1
            right += 1

    file.close()

if __name__ == '__main__':
    main()
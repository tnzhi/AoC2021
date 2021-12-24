from collections import defaultdict
import fileinput
inp = fileinput.input()

lines = [[int(b) for b in a.strip()] for a in inp]
# print(lines)

#make big map

bigmap = [[0 for i in range(len(lines[0]*5))] for j in range(len(lines)*5)]


for x in range(len(lines)):
    for y in range(len(lines[0])):
        bigmap[x][y] = lines[x][y]


for x in range(len(lines)):
    for y in range(len(lines[0])):
        for j in range(0,5):
            for i in range(0,5):
                if i == 0 and j == 0:
                    continue
                else:
                    bx = x + (i*len(lines[0]))
                    by = y + (j*len(lines))
                    value = 0
                    if i-1 >= 0:
                        px = x + ((i-1)*len(lines[0]))
                        py = y + ((j)*len(lines[0]))
                        value = (bigmap[px][py] + 1)
                    else:
                        px = x + ((i)*len(lines[0]))
                        py = y + ((j-1)*len(lines[0]))
                        value = (bigmap[px][py] + 1)
                    if value == 10:
                        value = 1
                    bigmap[bx][by] = value



for i in range(len(bigmap)):
    for j in range(len(bigmap)):
        print(bigmap[i][j], end="")
    print("")
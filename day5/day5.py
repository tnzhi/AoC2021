import fileinput
inp = fileinput.input()
from collections import defaultdict
subs = []
runningmax = 0
for sub in inp:
    a = sub.strip().split(" -> ")
    b = a[0].split(",")
    b = [int(b[0]), int(b[1])]
    c = a[1].split(",")
    c = [int(c[0]), int(c[1])]
    subs.append([b,c])
    runningmax = max(b[0],b[1],c[0],c[1],runningmax)


grid = [[0 for i in range(0,runningmax+1)] for i in range(0,runningmax+1)]
for sub in subs:
    x1 = sub[0][0]
    y1 = sub[0][1]
    x2 = sub[1][0]
    y2 = sub[1][1]
    if x1 == x2 or y1 == y2:
        if x1 == x2:
            start = min(y1,y2)
            end = max(y1,y2)
            for i in range(start,end+1):
                grid[i][x1] += 1
        if y1 == y2:
            start = min(x1,x2)
            end = max(x1,x2)
            for i in range(start,end+1):
                grid[y1][i] += 1
    elif x1 == y2 and x2 == y1 or ((x1-x2) == (y2-y1)) or ((x1-x2)==(y1-y2)):
        if x1 > x2 and y1 > y2:
            x = x1
            y = y1
            while True:
                grid[y][x] += 1
                if x == x2 and y == y2:
                    break
                print((x,y))
                x -= 1
                y -= 1
        elif x2 > x1 and y2 > y1:
            x = x2
            y = y2
            while True:
                grid[y][x] += 1
                if x == x1 and y == y1:
                    break
                x -= 1
                y -= 1
        elif x1 > x2:
            x = x1
            y = y1
            while True:
                grid[y][x] += 1
                if x == x2 and y == y2:
                    break
                x -= 1
                y += 1
        elif x2 > x1:
            x = x2
            y = y2
            while True:
                grid[y][x] += 1
                if x == x1 and y == y1:
                    break
                print((x,y))
                x -= 1
                y += 1

# (8,0) (0,8)

count = 0
for i in grid:
    print(i)
    for j in i:
        if j > 1:
            count += 1
print(count)
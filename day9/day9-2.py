import fileinput
inp = fileinput.input()
lines = [ [int(b) for b in a.strip()] for a in inp ]

def check(row,col,num):
    print(row,col)
    if row < 0:
        return True
    elif col < 0:
        return True
    elif col >= len(lines[0]):
        return True
    elif row >= len(lines):
        return True
    elif lines[row][col] > num:
        return True
    return False

lowpoints = []
for row in range(len(lines)):
    for col in range(len(lines[0])):
        num = lines[row][col]
        if check(row-1,col,num) and check(row,col-1,num) and check(row+1,col,num) and check(row,col+1,num):
            lowpoints.append((row,col))


def floodfill(row,col,num,visited):
    if (row,col) in visited:
        return
    if row < 0:
        return
    elif col < 0:
        return
    elif col >= len(lines[0]):
        return
    elif row >= len(lines):
        return
    elif lines[row][col] == 9:
        return
    # elif lines[row][col] < num:
    #     return
    else:
        visited.add((row,col))
        floodfill(row-1,col,num,visited)
        floodfill(row,col+1,num,visited)
        floodfill(row,col-1,num,visited)
        floodfill(row+1,col,num,visited)


found = []
for point in lowpoints:
    visited = set()
    floodfill(point[0],point[1],lines[point[0]][point[1]],visited)
    found.append(len(visited))

found.sort()
print(found[-1]*found[-2]*found[-3])
from collections import defaultdict
import fileinput
inp = fileinput.input()

dots = set()
folds = []

foldsstart = False
for line in inp:
    line = line.strip()
    if line == "":
        foldsstart = True
        continue
    if foldsstart == False:
        a,b = line.split(",")
        dots.add((int(a),int(b)))
    else:
        a,b = line.split()[2].split("=")
        folds.append((a,int(b)))

print(dots)

maxx = 1311
maxy = 895
# maxx = 11
# maxy = 15


newdots = set()
for fold in folds:
    newdots = set()
    if fold[0] == 'x':
        for dot in dots:
            x = dot[0]
            y = dot[1]
            if x >= fold[1]:
                newx = (maxx-x)-1
                newdots.add((newx,y))
                print(f"{(x,y)} -> {(newx,y)}")
            else:
                newdots.add((x,y))
        maxx = fold[1]
        
    if fold[0] == 'y':
        for dot in dots:
            x = dot[0]
            y = dot[1]
            if y >= fold[1]:
                newy = (maxy-y)-1
                newdots.add((x,newy))
                print(f"{(x,y)} -> {(x,newy)}")
            else:
                newdots.add((x,y))
        maxy = fold[1]
    dots = newdots


print(len(dots))

for i in range(maxy):
    for j in range(maxx):
        if (j,i) in dots:
            print("#", end="")
        else:
            print(".", end="")
    print("")
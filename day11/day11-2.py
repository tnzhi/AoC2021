import fileinput
inp = fileinput.input()
lines = [ [int(b) for b in a.strip()] for a in inp ]

numberFish = len(lines)*len(lines[0])

flashs = [0]

def flash(i,j):
    if i < 0 or i >= len(lines):
        return
    if j < 0 or j >= len(lines):
        return
    if lines[i][j] == 0:
        return
    lines[i][j] += 1
    if lines[i][j] > 9:
        flashs[0] += 1
        lines[i][j] = 0
        flash(i-1,j-1)
        flash(i-1,j)
        flash(i,j-1)
        flash(i+1,j+1)
        flash(i+1,j)
        flash(i,j+1)
        flash(i-1,j+1)
        flash(i+1,j-1)

days = 0
while True:
    days += 1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] += 1

    flashs = [0]

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] > 9:
                lines[i][j] -= 1
                flash(i,j)

    if flashs[0] == numberFish:
        print(days)
        break

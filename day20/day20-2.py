from collections import defaultdict
import fileinput

### Get input
inp = fileinput.input()
algo = list(next(inp).strip())

# print(enhancealgo)
inputimage = []
_ = next(inp)
while True:
    try:
        line = next(inp).strip()
    except StopIteration:
        break
    inputimage.append(list(line))

# scanners.append(currentscanner)
def iprint(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
            print(image[i][j],end="")
        print("")

def pad(image, char):
    for row in image:
        row.insert(0, char)
        row.append(char)
    paddrow = [char for _ in range(len(image[0]))]
    image.append(paddrow)
    image.insert(0, paddrow[:])


def pixelEnchance(r,c,image):
    code = image[r-1][c-1] + image[r-1][c] + image[r-1][c+1] + image[r][c-1] + image[r][c] + image[r][c+1] + image[r+1][c-1] + image[r+1][c] + image[r+1][c+1]
    # print(code)
    bincode = "".join([ "0" if c == "." else "1" for c in code ])
    # print(bincode)
    num = int(bincode,2)
    return algo[num]
    # print(num)

def enchance(inputimage, char="."):
    newimage = [[char for _ in range(len(inputimage[0]))] for __ in range(len(inputimage))]
    for r in range(1,len(inputimage)-1):
        for c in range(1,len(inputimage[0])-1):
            newimage[r][c] = pixelEnchance(r,c,inputimage)
    return newimage

flip = True
for i in range(50):
    if flip:
        pad(inputimage,".")
        pad(inputimage,".")
        inputimage = enchance(inputimage,"#")
    else:
        pad(inputimage,"#")
        pad(inputimage,"#")
        inputimage = enchance(inputimage,".")
    flip = not flip

count = 0
for i in inputimage:
    for j in i:
        if j == "#":
            count+=1

print(count)
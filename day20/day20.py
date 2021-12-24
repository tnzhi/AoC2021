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

iprint(inputimage)
pad(inputimage,".")
pad(inputimage,".")
# print("----------")
# iprint(inputimage)
# print("----------")

output = enchance(inputimage,"#")
print("")
iprint(output)

pad(output,"#")
pad(output,"#")
output2 = enchance(output)
print("")
iprint(output2)

count = 0
for i in output2:
    for j in i:
        if j == "#":
            count+=1

print(count)
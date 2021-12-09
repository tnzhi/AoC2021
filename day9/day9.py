import fileinput
inp = fileinput.input()
lines = [ [int(b) for b in a.strip()] for a in inp ]
print(lines)

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

ans = []
for row in range(len(lines)):
    for col in range(len(lines[0])):
        num = lines[row][col]
        if check(row-1,col,num) and check(row,col-1,num) and check(row+1,col,num) and check(row,col+1,num):
            ans.append(num+1)


print(sum(ans))
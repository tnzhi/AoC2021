import fileinput

inp = fileinput.input()
lines = [ [b.split() for b in a.strip().split("|")] for a in inp ]
print(lines)


count = 0
for line in lines:
    for a in line[1]:
        if len(a) in [2,4,3,7]:
            count += 1
            print(f"{a} <-")
        else:
            print({a})


print(count)


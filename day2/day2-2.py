import fileinput

# for line in fileinput.input():
#     print(line.rstrip('\n'))

inp = fileinput.input()
subs = [a.strip().split() for a in inp]
hoz = 0
dep = 0
aim = 0
for i in subs:
    if i[0] == 'forward':
        hoz += int(i[1])
        dep += int(i[1])*aim
    elif i[0] == 'up':
        aim -= int(i[1])
    elif i[0] == 'down':
        aim += int(i[1])
    else:
        print("error")

print(hoz*dep)
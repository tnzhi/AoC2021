import fileinput

# for line in fileinput.input():
#     print(line.rstrip('\n'))

inp = fileinput.input()
subs = [int(a) for a in inp]


increasing = 0
for i in range(3,len(subs)):
    if subs[i] > subs[i-3]:
        increasing += 1

print(increasing)
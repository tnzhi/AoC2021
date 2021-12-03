import fileinput

# for line in fileinput.input():
#     print(line.rstrip('\n'))

inp = fileinput.input()
subs = [int(a) for a in inp]
increasing = 0
for i in range(1,len(subs)):
    if subs[i] > subs[i-1]:
        increasing += 1

print(range(1,len(subs)))
from collections import defaultdict
import fileinput
inp = fileinput.input()

template = []
inserts = {}

foldsstart = False
for line in inp:
    line = line.strip()
    if line == "":
        foldsstart = True
        continue
    if foldsstart == False:
        template = line
    else:
        a,b = line.split(" -> ")
        inserts[a] = b

print(template)
print(inserts)

days = 10
for day in range(days):
    newtemplate = []
    for i in range(1,len(template)):
        pair = template[i-1] + template[i]
        if pair in inserts.keys():
            newtemplate.append(template[i-1])
            newtemplate.append(inserts[pair])
        else:
            newtemplate.append(template[i-1])

    newtemplate.append(template[-1])
    template = "".join(newtemplate)
    
letters = defaultdict(int)
for l in template:
    letters[l] += 1

minx = min(letters.values())
maxx = max(letters.values())
print(maxx - minx)



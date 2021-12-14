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

pairs = defaultdict(int)
letters = defaultdict(int)

for i in range(1,len(template)):
    pair = template[i-1] + template[i]
    letters[template[i-1]] += 1
    pairs[pair] += 1
letters[template[-1]] += 1

days = 40
newpairs = defaultdict(int)
for day in range(days):
    newpairs = defaultdict(int)
    for pair in pairs:
        if pairs[pair] == 0:
            continue
        if pair in inserts.keys():
            newpair = inserts[pair] + pair[1]
            newpair2 =  pair[0] + inserts[pair]
            newpairs[newpair] += pairs[pair]
            newpairs[newpair2] += pairs[pair]

            letters[inserts[pair]] += pairs[pair]
        else:
            newpairs[pair] = pairs[pair]

    pairs = newpairs

minx = min(letters.values())
maxx = max(letters.values())
print(minx)
print(maxx)

print(maxx-minx)
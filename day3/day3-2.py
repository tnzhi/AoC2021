import fileinput

NUMBITS = 12
inp = fileinput.input()
lines = [int(line,2) for line in inp]

filters = [None for i in range(NUMBITS)]
def criteria(line):
    for i in range(NUMBITS):
        if filters[i] != None and (line >> i & 1) != filters[i]:
            return False
    return True

for i in range(NUMBITS-1,-1,-1):
    counts = 0
    filteredlines = list(filter(criteria, lines))
    if len(filteredlines) == 1:
        break
    for line in filteredlines:
        counts += line >> i & 1
    mostfreq = 1 if counts >= len(filteredlines)/2 else 0
    filters[i] = mostfreq

oxyrating = list(filter(criteria, lines))[0]

filters = [None for i in range(NUMBITS)]

for i in range(NUMBITS-1,-1,-1):
    counts = 0
    filteredlines = list(filter(criteria, lines))
    if len(filteredlines) == 1:
        break
    for line in filteredlines:
        counts +=  line >> i & 1
    mostfreq = 0 if counts >= len(filteredlines)/2 else 1
    filters[i] = mostfreq

co2rating = list(filter(criteria, lines))[0]

print(oxyrating * co2rating)

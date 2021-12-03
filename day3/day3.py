import fileinput

NUMBITS = 12
inp = fileinput.input()
subs = [int(a,2) for a in inp]

counts = [0 for i in range(NUMBITS)]
for sub in subs:
    for i in range(NUMBITS):
        counts[i] +=  (1<<i & sub) >> i

mostfreq = 0
lestfreq = 0
for i in range(NUMBITS):
    if counts[i] > len(subs)/2:
        mostfreq += 1 << i
    else:
        lestfreq += 1 << i

print(mostfreq*lestfreq)
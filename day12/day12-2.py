from collections import defaultdict
import fileinput
inp = fileinput.input()
lines = [a.strip() for a in inp ]

graph = defaultdict(list)
for line in lines:
    a,b = line.split("-")
    graph[a].append(b)
    graph[b].append(a)


alllower = [ i for i in graph.keys() if i.islower() and i != 'start' and i != 'end']

paths = []

def findpath(node,path,twicelowercase):
    ppath = path[:]
    ppath.append(node)

    if node == 'end':
        paths.append(ppath)
        return
    else:
        for newnode in graph[node]:
            if newnode == 'start':
                continue
            if newnode == twicelowercase:
                if ppath.count(newnode) < 2:
                    findpath(newnode,ppath, twicelowercase)
                else:
                    continue
            else:
                if newnode.islower() and (newnode in ppath):
                    continue
                else:
                    findpath(newnode,ppath, twicelowercase)


for lower in alllower:
    path = []
    twicelowercase = None
    findpath('start',path,lower)

uniquepaths = set()
for i in paths:
    uniquepaths.add("".join(i))
print(len(uniquepaths))

from collections import defaultdict
import fileinput
inp = fileinput.input()
lines = [a.strip() for a in inp ]

graph = defaultdict(list)
for line in lines:
    a,b = line.split("-")
    graph[a].append(b)
    graph[b].append(a)

paths = []

def findpath(node,path):
    ppath = path[:]
    ppath.append(node)

    if node == 'end':
        paths.append(ppath)
        return
    if node == 'start':
        return
    else:
        for newnode in graph[node]:
            if (newnode.islower() and (newnode in ppath)) or newnode == 'start':
                continue
            else:
                findpath(newnode,ppath)


ans = 0
for node in graph['start']:
    path = []
    findpath(node,path)

print(len(paths))
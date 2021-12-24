from collections import defaultdict
import fileinput
inp = fileinput.input()
import heapq
lines = [[int(b) for b in a.strip()] for a in inp]
# print(lines)

dist = {}
prev = {}

def getNeighbor(node):
    x = node[0]
    y = node[1]
    nodes = []
    node1 = (x-1,y)
    if x-1 >= 0:
        nodes.append(node1)
    node2 = (x,y-1)
    if y-1 >= 0:
        nodes.append(node2)
    node3 = (x+1,y)
    if x+1 < len(lines[0]):
        nodes.append(node3)
    node4 = (x,y+1)
    if y+1 < len(lines):
        nodes.append(node4)
    return nodes


def dij(start):
    Q = [(0, start)]
    setQ = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            dist[(i,j)] = 99999999
            prev[(i,j)] = None
            Q.append((99999999,(i,j)))
            setQ.add((i,j))
    dist[start] = 0
    while len(Q):
        current_distance, u = heapq.heappop(Q)
        for node in getNeighbor(u):
            alt = dist[u] + lines[node[0]][node[1]]
            if alt < dist[node]:
                dist[node] = alt
                prev[node] = u
                heapq.heappush(Q, (alt, node))

dij((0,0))
print(dist[(len(lines)-1,len(lines)-1)])
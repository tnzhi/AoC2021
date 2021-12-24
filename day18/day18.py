import math
from collections import namedtuple
import fileinput
inp = fileinput.input()
lines = [eval(a.strip()) for a in inp ]

StarfishNumber = namedtuple("StarfishNumber", "num path")

# starfish = [[[[[9,8],1],2],3],4]
# starfish = [7,[6,[5,[4,[3,2]]]]]
# starfish = [[6,[5,[4,[3,2]]]],1]
# starfish = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

# starfish = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

# starfish =  [ [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]] , [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]

def addFish(star1, star2):
    return [star1, star2]

def flatten(star, flattenedtree, path):
    left = star[0]
    right = star[1]

    leftpath = path[:]
    leftpath.append(0)
    if type(left) == int:
        flattenedtree.append(StarfishNumber(left, leftpath))
    else:
        flatten(left, flattenedtree, leftpath)
    
    rightpath = path[:]
    rightpath.append(1)
    if type(right) == int:
        flattenedtree.append(StarfishNumber(right, rightpath))
    else:
        flatten(right, flattenedtree, rightpath)

def deletePair(tree, pair):
    left, right = pair
    path = left.path[:-2]
    for i in path:
        tree = tree[i]
    tree[left.path[-2]] = 0

def setTree(tree, value, path):
    newpath = path[:-1]
    for i in newpath:
        tree = tree[i]
    tree[path[-1]] = value

def explode(star):
    flatTree = []
    flatten(star, flatTree, [])
    firstPairToExplode = None
    firstPairToExplodeIndex = None
    for i in range(len(flatTree)-1):
        num, path = flatTree[i]
        nextNum, nextPath = flatTree[i+1]
        if len(path) == 5 and len(nextPath) == 5:
            firstPairToExplode = (flatTree[i], flatTree[i+1])
            firstPairToExplodeIndex = (i,i+1)
            break
    
    if firstPairToExplode != None:
        deletePair(star, firstPairToExplode)
        #redistrube values
        left, right = (firstPairToExplode)
        lefti, righti = (firstPairToExplodeIndex)
        if lefti-1 >= 0:
            newleftvalue = flatTree[lefti-1].num + left.num
            newleftpath = flatTree[lefti-1].path
            setTree(star, newleftvalue, newleftpath)

        if righti+1 < len(flatTree):
            newrightvalue = flatTree[righti+1].num + right.num
            newrightpath = flatTree[righti+1].path
            setTree(star, newrightvalue, newrightpath)
        return True
    return False


def explodeUntilDone(starfish):
    didExplode = False
    while True:
        exploded = explode(starfish)
        if exploded:
            didExplode = True
        else:
            break
    return didExplode


def split(star):
    didSplit = False
    if type(star[0]) is int:
        if star[0]>9:
            star[0] = [math.floor(star[0]/2), math.ceil(star[0]/2)]
            didSplit = True
            return didSplit
    else:
        didSplit = split(star[0])
        if didSplit: return didSplit
    
    if type(star[1]) is int :
        if star[1]>9:
            star[1] = [math.floor(star[1]/2), math.ceil(star[1]/2)]
            didSplit = True
            return didSplit
    else:
        didSplit = split(star[1])
        if didSplit: return didSplit


    return didSplit


def reduce(starfish):
    while True:
        didExplode = explodeUntilDone(starfish)
        didSplit = split(starfish)
        if didExplode == False and didSplit == False:
            break
    return starfish
    
        
def magnitude(star):
    left = star[0]
    right = star[1]
    leftvalue = 0
    if type(left) is int:
        leftvalue = left
    else:
        leftvalue = magnitude(left)
    
    if type(right) is int:
        rightvalue = right
    else:
        rightvalue = magnitude(right)

    return leftvalue*3 + rightvalue*2



runningsum = lines[0]
for i in range(1,len(lines)):
    runningsum = addFish(runningsum,lines[i])
    reduce(runningsum)

print(magnitude(runningsum))

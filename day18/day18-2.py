import math
from collections import namedtuple
import fileinput
inp = fileinput.input()
lines = [eval(a.strip()) for a in inp ]
StarfishNumber = namedtuple("StarfishNumber", "num path")

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


import copy
maxsum = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i!=j:

            fish1 = copy.deepcopy(lines[i])
            fish2 = copy.deepcopy(lines[j])
            fish = addFish(fish1,fish2)
            reduce(fish)
            maxsum = max(magnitude(fish), maxsum)

print(maxsum)
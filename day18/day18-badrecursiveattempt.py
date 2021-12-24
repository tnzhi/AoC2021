import math
starfish = [[[[[9,8],1],2],3],4]
starfish = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
starfish = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
starfish = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

starfish = [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]

def explode(star, depth):
    l = 0
    r = 0
    didExplode = False
    if depth == 5:
        return (star[0],star[1],True)

    depth += 1
    # if left is list recurse left
    if type(star[0]) is list:
        left = explode(star[0],depth)

    # if right is list recurse right
    if type(star[1]) is list:
        right = explode(star[1],depth)

    # if left is int and right exploded and rightexplode
    if type(star[0]) is int and type(star[1]) is list:
        star[0] += right[0]
        if depth == 5:
            star[1] = 0
            l = 0
            r = right[1]
            didExplode = True

    # if right in int and left exploded and leftedexploded
    if type(star[1]) is int and type(star[0]) is list:
        star[1] += left[1]
        if depth == 5:
            star[0] = 0
            l = left[0]
            r = 0
            didExplode = True

    if type(star[0]) and type(star[1]):
        


    if type(star[0]) is list:
        l = left[0]
        r = left[1]
    if type(star[1]) is list:
        l = right[0]
        r = right[1]
    if type(star[0]) is list and type(star[1]) is list:
        l = left[0]
        r = right[1]
    
    return (l,r, didExplode)

def split(star):
    didSplit = False
    if type(star[0]) is int:
        if star[0]>9:
            star[0] = [math.floor(star[0]/2), math.ceil(star[0]/2)]
            didSplit = True
    else:
        split(star[0])
    
    if type(star[1]) is int :
        if star[1]>9:
            star[1] = [math.floor(star[1]/2), math.ceil(star[1]/2)]
            didSplit = True
    else:
        split(star[1])

    return didSplit

# print(reduce(starfish))

print(starfish)
explode(starfish,1)
print(starfish)
player1 = 6
player2 = 1
# player1 = 4
# player2 = 8


player1points = 0
player2points = 0

def getPost(pos, diceroll):
    positions = [i for i in range(1,11)]
    posi = pos - 1
    posi = (posi + diceroll) % 10
    return positions[posi]

memo = {}
def solve(p1pos, p2pos, p1points, p2points, isp1Turn):
    if (p1pos, p2pos, p1points, p2points, isp1Turn) in memo:
        return memo[(p1pos, p2pos, p1points, p2points, isp1Turn)]

    if not isp1Turn and p1points >= 21:
        memo[(p1pos, p2pos, p1points, p2points, isp1Turn)] = (1,0)
        return (1,0)
    if isp1Turn and p2points >= 21:
        memo[(p1pos, p2pos, p1points, p2points, isp1Turn)] = (0,1)
        return (0,1)
    
    if isp1Turn:
        count = [0,0]
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    dice = i + j + k
                    newpos = getPost(p1pos, dice)
                    newpoints = p1points + newpos
                    a = solve(newpos, p2pos, newpoints, p2points, False)
                    count[0] += a[0]
                    count[1] += a[1]
        memo[(p1pos, p2pos, p1points, p2points, isp1Turn)] = (count[0],count[1])
        return (count[0],count[1])

    else:
        count = [0,0]
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    dice = i + j + k
                    newpos = getPost(p2pos, dice)
                    newpoints = p2points + newpos
                    a = solve(p1pos, newpos, p1points, newpoints, True)
                    count[0] += a[0]
                    count[1] += a[1]
        
        memo[(p1pos, p2pos, p1points, p2points, isp1Turn)] = (count[0],count[1])
        return (count[0],count[1])
    

    



print(solve(player1, player2, 0, 0, True))
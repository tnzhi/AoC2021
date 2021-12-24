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



# print(getPost(1,100))



dice = 1
positions = [i for i in range(1,11)]
print(positions)
currentplayerisplayer1 = True
currentplayer = player1
while True:
    rolldice = dice
    dice +=1
    rolldice1 = dice
    dice +=1
    rolldice2 = dice
    dice +=1
    # newpos = currentplayer + rolldice + rolldice1 + rolldice2
    newpos = getPost(currentplayer, rolldice + rolldice1 + rolldice2)
    # print(newpos)

    currentplayer = newpos
    if currentplayerisplayer1:
        player1 = currentplayer
        player1points += currentplayer
        currentplayer = player2
        currentplayerisplayer1 = False
        if player1points >= 1000:
            break
    else:
        player2 = currentplayer
        player2points += currentplayer
        currentplayer = player1
        currentplayerisplayer1 = True
        if player2points >= 1000:
            break




# print(player1)
print("---")
print(player1points)
print(player2points)
print(dice)
dice -= 1
print(dice*min(player1points, player2points))
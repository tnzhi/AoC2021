SIZE = 5

import fileinput

inp = fileinput.input()
subs = [a.strip() for a in inp]

numbs = [int(a) for a in subs[0].split(",")]
subs = subs[2:]
boards = []
while True:
    board = []
    for j in range(SIZE):
        board.append([[int(a),0] for a in subs[0].split()])
        subs = subs[1:]
    subs = subs[1:]
    boards.append(board)
    if len(subs) < 1:
        break

numboards = len(boards)


def simulate(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j][0] == num:
                board[i][j][1] = 1
                
# print(boards[1])
def checkwinner(board):
    # checkcolumn
    count = 0
    for i in range(SIZE):
        count = 0
        for j in range(SIZE):
            count += board[i][j][1]
        if count == SIZE:
            return True
    # checkrows
    count = 0
    for i in range(SIZE):
        count = 0
        for j in range(SIZE):
            count += board[j][i][1]
        if count == SIZE:
            return True
    return False

winners = []
winnernum = 0
winnersindex = set()
for num in numbs:
    flag = False
    for i in range(numboards):
        if not (i in winnersindex):
            # print(i)
            simulate(boards[i], num)
            if checkwinner(boards[i]):
                print("winner")
                print(i)
                winners.append(boards[i])
                winnernum = num
                winnersindex.add(i)
                # boards.remove(board)
                if len(winners) == numboards:
                    flag = True
                    break

    

# calc winner
winner = winners[-1]
# print(winners)
sumsss=0
for i in range(SIZE):
    for j in range(SIZE):
        if winner[i][j][1] == 0:
            sumsss += winner[i][j][0]

print(sumsss * winnernum)


# for i in range(numboards):
#     print(winners[i])
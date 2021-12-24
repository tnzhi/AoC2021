target = "x=20..30, y=-10..-5"
# target area: x=150..171, y=-129..-70

xtarget = (150,171)
ytarget = (-129,-70)
# xtarget = (10,30)
# ytarget = (-10,-5)

probestart = (0,0)

probe = [0,0]


memo = {}

def simulate(vx,vy):
    vx = vx
    vy = vy
    maxh = 0
    x = 0
    y = 0
    while True:
        x = x+vx
        vx -= 1
        if vx<0: 
            vx = 0
        y = y+vy
        maxh = max(maxh, y)
        vy -=1
        if x <= xtarget[1]  and x >= xtarget[0] and y <= ytarget[1] and y >= ytarget[0]:
            return maxh
        if y < ytarget[0]:
            return -100
    return maxh


nopex = set()
okx = set()
def simulatex(vx):
    vx = vx
    x = 0
    while True:
        x = x+vx
        vx -= 1
        if vx<0: 
            vx = 0
        if x <= xtarget[1]  and x >= xtarget[0]:
            okx.add(okx)
            return True
        if x > xtarget[1]:
            nopex.add(vx)
            return False

nopey = set()
oky = {}
def simulate(vy):
    vy = vy
    maxh = 0
    y = 0
    while True:
        y = y+vy
        maxh = max(maxh, y)
        vy -=1
        if y <= ytarget[1] and y >= ytarget[0]:
            oky[vy] = maxh
            return True
        if y < ytarget[0]:
            nopey.add(vy)
            return False




for i in range(1000):
    simulatex(i)
for i in range(1000):
    simulatey(i)

ans = 0
for i in range(1000):
    for j in range(1000):
        if 
            ans = max(simulate(i,j), ans)
print(ans)

# print(simulate(6,3))
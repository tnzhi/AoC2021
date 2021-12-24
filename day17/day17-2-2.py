target = "x=20..30, y=-10..-5"
# target area: x=150..171, y=-129..-70

# xtarget = (150,171)
# ytarget = (-129,-70)
xtarget = (10,30)
ytarget = (-10,-5)

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


ans = 0
answers = []
for i in range(1000):
    for j in range(-100,100):
        ans = max(simulate(i,j), ans)
        if ans != -100 and ans != 0:
            answers.append((i,j))
print(len(answers))

# print(simulate(6,3))
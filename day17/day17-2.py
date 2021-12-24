# target = "x=20..30, y=-10..-5"
# target area: x=150..171, y=-129..-70

xtarget = (150,171)
ytarget = (-129,-70)
# xtarget = (20,30)
# ytarget = (-10,-5)

probestart = (0,0)

probe = [0,0]


memo = {}

# def simulate(vxx,vyy):
#     vx = vxx
#     vy = vyy
#     maxh = 0
#     x = 0
#     y = 0
#     while True:
#         x = x+vx
#         vx -= 1
#         if vx<0:
#             vx = 0
#             if x < xtarget[0]:
#                 return -100
#         y = y+vy
#         maxh = max(maxh, y)
#         vy -=1
#         if x <= xtarget[1]  and x >= xtarget[0] and y <= ytarget[1] and y >= ytarget[0]:
#             return maxh
#         if y < ytarget[0]:
#             return -100
#     return maxh

def simulate(vxx,vyy):
    vx = vxx
    vy = vyy
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
        if (x <= xtarget[1]  and x >= xtarget[0]) and (y <= ytarget[1] and y >= ytarget[0]):
            return maxh
        if y < ytarget[0]:
            return -100
    return maxh

nopex = set()
okx = set()
def simulatex(vx):
    vxnew = vx
    x = 0
    while True:
        x = x+vxnew
        vxnew -= 1
        if vxnew<0: 
            vxnew = 0
            if not (x <= xtarget[1]  and x >= xtarget[0]):
                nopex.add(vx)
                return False
            # nopex.add(vx)
            # return False
        if x <= xtarget[1]  and x >= xtarget[0]:
            okx.add(vx)
            return True
        if x > xtarget[1]:
            nopex.add(vx)
            return False

nopey = set()
oky = {}
def simulatey(vy):
    vynew = vy
    maxh = 0
    y = 0
    while True:
        y = y+vynew
        maxh = max(maxh, y)
        vynew -=1
        if y <= ytarget[1] and y >= ytarget[0]:
            oky[vy] = maxh
            return True
        if y < ytarget[0]:
            nopey.add(vy)
            return False




for i in range(1000):
    simulatex(i)
for i in range(-1000,1000):
    simulatey(i)

# ans = 0
# for i in range(1000):
#     for j in range(1000):
#         if 
#             ans = max(simulate(i,j), ans)
# print(ans)

# print(simulate(6,3))

print(len(okx) * len(oky))
print(okx)
print(oky.keys())

ans = set()
# for i in range(100):
#     for j in range(-100,100):
#         if i in okx and j in oky.keys():
#             ans.add((i,j))

# bads = set()

for i in okx:
    for j in oky.keys():
        maxh = simulate(i,j)
        if maxh != -100:
            ans.add((i,j))
        # else:
        #     bads.add((i,j))


print(len(ans))
# count= 9
# for i in ans:
#     if count == 0:
#         break
#     count -= 1
#     print(i)
# print(simulate(4,9))
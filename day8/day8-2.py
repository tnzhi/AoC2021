import fileinput

inp = fileinput.input()
lines = [ [b.split() for b in a.strip().split("|")] for a in inp ]

# ['a','b','c','d','e','f','g']
#
#  aaa
# b   c
# b   c
#  ddd
# e   f
# e   f
#  ggg
#
nums = [
    [1,1,1,0,1,1,1], #0
    [0,0,1,0,0,1,0], #1
    [1,0,1,1,1,0,1], #2
    [1,0,1,1,0,1,1], #3
    [0,1,1,1,0,1,0], #4
    [1,1,0,1,0,1,1], #5
    [1,1,0,1,1,1,1], #6
    [1,0,1,0,0,1,0], #7
    [1,1,1,1,1,1,1], #8
    [1,1,1,1,0,1,1]  #9
  ]


def isPossible(combo, numletters):
    sss = []
    for letter in combo:
        if letter in numletters:
            sss.append(1)
        else:
            sss.append(0)
    if sss in nums:
        return True
    else:
        return False

def decode(combo, numletters):
    sss = []
    for letter in combo:
        if letter in numletters:
            sss.append(1)
        else:
            sss.append(0)
    if sss in nums:
        return str(nums.index(sss))
    else:
        return False



from itertools import permutations
totalsum = 0 
for line in lines:
    foundcombo = None
    for combo in permutations(['a','b','c','d','e','f','g']):
        possibles = 0
        for number in line[0]:
            if not isPossible(combo, number):
                # print(f"False {number} {combo}")
                found = False
                break
            else:
                possibles += 1
        if possibles == len(line[0]):
            foundcombo = combo
            # print("FOUND COMBO")
            break

    # print(foundcombo)
    answer = []
    for ss in line[1]:
        answer.append(decode(foundcombo,ss))
    # print("".join(answer))
    totalsum += int("".join(answer))


# print(decode(['a','b','c','d','e','f','g'],'cf'))
# print(count)
print(totalsum)

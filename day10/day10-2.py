import fileinput
inp = fileinput.input()
lines = [ a.strip() for a in inp ]

points = 0
incompletelines = []
for line in lines:
    stack = []
    flag = False
    for brack in line:
        if brack == '{':
            stack.append('{')
        if brack == '(':
            stack.append('(')
        if brack == '[':
            stack.append('[')
        if brack == '<':
            stack.append('<')
        if brack == '}':
            s = stack.pop()
            if s != '{':
                flag= True
                points += 1197
                break
        if brack == ')':
            s = stack.pop()
            if s != '(':
                flag= True
                points += 3
                break
        if brack == ']':
            s = stack.pop()
            if s != '[':
                flag= True
                points += 57
                break
        if brack == '>':
            s = stack.pop()
            if s != '<':
                flag= True
                points += 25137
                break
    if flag == False:
        incompletelines.append(line)

totalscores = []
for line in incompletelines:
    stack = []
    for brack in line:
        if brack == '{':
            stack.append('{')
        if brack == '(':
            stack.append('(')
        if brack == '[':
            stack.append('[')
        if brack == '<':
            stack.append('<')
        if brack == '}':
            s = stack.pop()
        if brack == ')':
            s = stack.pop()
        if brack == ']':
            s = stack.pop()
        if brack == '>':
            s = stack.pop()
    score = 0
    stack.reverse()
    for brack in stack:
        score *= 5
        if brack == '{':
            score += 3
        if brack == '(':
            score += 1
        if brack == '[':
            score += 2
        if brack == '<':
            score += 4

    totalscores.append(score)

totalscores.sort()
print(totalscores)
print(totalscores[int(len(totalscores)/2)])
import fileinput
inp = fileinput.input()
lines = [ a.strip() for a in inp ]

points = 0
for line in lines:
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
            if s != '{':
                points += 1197
                break
        if brack == ')':
            s = stack.pop()
            if s != '(':
                points += 3
                break
        if brack == ']':
            s = stack.pop()
            if s != '[':
                points += 57
                break
        if brack == '>':
            s = stack.pop()
            if s != '<':
                points += 25137
                break

print(points)
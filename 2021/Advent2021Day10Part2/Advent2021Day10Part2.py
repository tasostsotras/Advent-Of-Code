from statistics import median


def checker(line):
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        elif char in ')':
            if stack.pop() != '(':
                return 0
        elif char in ']':
            if stack.pop() != '[':
                return 0
        elif char in '}':
            if stack.pop() != '{':
                return 0
        elif char in '>':
            if stack.pop() != '<':
                return 0
    score = 0
    d = {'(': 1, '[': 2, '{': 3, '<': 4}
    for char in stack[::-1]:
        score *= 5
        score += d[char]
    return score


data = open('C:/Users/tasos/Downloads/input10partone.txt', 'r', encoding="utf-8").read().splitlines()
scores = [checker(line) for line in data]
print(median([x for x in scores if x != 0]))

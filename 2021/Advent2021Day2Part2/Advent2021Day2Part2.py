data = open('C:/Users/tasos/Downloads/input2partone.txt', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data]
commands = [(x[0], int(x[1])) for x in data]

aim, h, d = 0, 0, 0

for cmd, val in commands:
    if cmd == 'forward':
        h += val
        d += val * aim
    elif cmd == 'down':
        aim += val
    elif cmd == 'up':
        aim -= val
    else:
        raise ValueError('Invalid command')

print(h * d)

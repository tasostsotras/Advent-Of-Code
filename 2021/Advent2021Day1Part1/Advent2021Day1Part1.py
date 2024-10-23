data = open('C:/Users/tasos/Downloads/input1partone.txt', 'r', encoding='utf-8').read().splitlines()
depths = [int(x) for x in data]
increases = sum(x < y for x, y in zip(depths, depths[1:]))
print(increases)
# 1342

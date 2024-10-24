from collections import Counter

data = open('C:/Users/tasos/Downloads/input6partone.txt', 'r', encoding='utf-8').read()
df = Counter([int(x) for x in data.split(",")])
for i in range(-1, 9):
    if i not in df:
        df[i] = 0

for day in range(256):
    for i in range(9):
        df[i-1] = df[i]
    df[6] += df[-1]
    df[8] = df[-1]
    df[-1] = 0
    print(f"After {day+1} days:", df)

total = 0
for i in range(9):
    total += df[i]
print(total)

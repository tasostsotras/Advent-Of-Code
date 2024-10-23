data = open('C:/Users/tasos/Downloads/input7partone.txt', 'r', encoding='utf-8').read()
df = list(map(int, data.split(',')))
p_min, p_max = min(df), max(df)
fuels = [sum(map(lambda x: abs(x - p) * (abs(x - p) + 1) // 2, df)) for p in range(p_min, p_max + 1)]
print(min(fuels))

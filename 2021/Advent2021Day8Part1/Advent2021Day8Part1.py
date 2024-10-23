import numpy as np

data = open('C:/Users/tasos/Downloads/input8partone.txt', 'r', encoding='utf-8').read().splitlines()
data = [x.split('|') for x in data]
data = [(i.split(), o.split()) for i,o in data]

total = 0
for d in data:
    nb_segments = [len(x) for x in d[1]]
    nb_segments = np.array(nb_segments)
    is1 = (nb_segments == 2).sum()
    is4 = (nb_segments == 4).sum()
    is7 = (nb_segments == 3).sum()
    is8 = (nb_segments == 7).sum()
    total += is1 + is4 + is7 + is8

print(total)

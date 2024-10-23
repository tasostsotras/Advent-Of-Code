import numpy as np
from skimage.measure import label, regionprops

df = np.array([list(map(int, [c for c in line])) for line in open('C:/Users/tasos/Downloads/input9partone.txt', 'r', encoding="utf-8").read().splitlines()])
print(np.prod(sorted([r.area for r in regionprops(label(df < 9, connectivity=1))])[-3:]))

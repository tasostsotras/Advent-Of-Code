import numpy as np
from scipy import signal

data = open('C:/Users/tasos/Downloads/input11partone.txt', 'r', encoding='utf-8').read().splitlines()
df = np.array([[int(x) for x in line] for line in data])

step = 0
while True:
    energy = np.ones_like(df)
    flashed = np.zeros_like(df)
    while np.any(energy.astype(bool)):
        df += energy
        flashing = np.logical_and((df > 9), np.logical_not(flashed))
        energy = signal.convolve(flashing, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same')
        flashed = np.logical_or(flashed, flashing)
    df[flashed] = 0
    step += 1
    if np.all(flashed):
        print(step)
        exit()

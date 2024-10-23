import numpy as np


banks = np.array([0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11], dtype=np.int64)
seen_banks = []
num_banks = len(banks)
cycles = 0
while True:
    seen_banks.append(np.copy(banks))
    highest = np.argmax(banks)
    blocks = banks[highest]
    rounds = blocks // num_banks
    extra = blocks % num_banks
    indices = (highest + 1 + np.arange(extra)) % (num_banks)
    banks[highest] = 0
    banks[indices] += 1
    banks += np.repeat(rounds, num_banks)
    if any(np.all(old_banks == banks) for old_banks in seen_banks):
        break

# Part one
print(len(seen_banks))

# Part two
print(len(seen_banks) - np.argmax([np.all(old_banks == banks) for old_banks in seen_banks]))

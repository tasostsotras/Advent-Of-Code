from itertools import count


def solve(ns, ps):
    for i in count():
        if all((ps[k] + i + k + 1) % ns[k] == 0 for k in range(len(ns))):
            return i


print(solve([17, 19, 7, 13, 5, 3], [5, 8, 1, 7, 1, 0]))
print(solve([17, 19, 7, 13, 5, 3, 11], [5, 8, 1, 7, 1, 0, 0]))

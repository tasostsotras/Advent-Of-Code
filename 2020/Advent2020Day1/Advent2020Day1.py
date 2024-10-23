def part1(nums):
    for i in nums:
        for j in nums:
            if i + j == 2020:
                return i * j


def part2(nums):
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    return i * j * k


with open('input1partone.txt') as f:
    inputs = [
        int(line)
        for line in f.read().splitlines()
    ]
    print(part1(inputs))
    print(part2(inputs))

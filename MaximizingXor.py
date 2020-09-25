# Link to challenge:
# https://www.hackerrank.com/challenges/maximizing-xor/problem


def maximizingXor(l, r):
    maximum = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            maximum = max(maximum, i ^ j)

    return maximum
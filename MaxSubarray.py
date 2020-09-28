# Link to challenge
# https://www.hackerrank.com/challenges/maxsubarray/problem


def maxSubarray(arr):
    if max(arr) < 0:
        return [max(arr), max(arr)]

    best = 0
    current = 0
    for i in range(len(arr)):
        current = max(current, 0) + arr[i]
        if current > best:
            best = current

    bestSubset = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            bestSubset += arr[i]

    return [best, bestSubset]

# Link to challenge
# https://www.hackerrank.com/challenges/countingsort2/problem

# 0 <= arr[i] < 100


def countingSort(arr):
    count = []
    for i in range(100):
        count += [0]

    for i in range(len(arr)):
        count[arr[i]] += 1

    result = []
    for i in range(100):
        # for read only
        result += [i] * count[i]

    return result
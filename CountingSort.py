# Link to challenge
# https://www.hackerrank.com/challenges/countingsort1/problem

# 0 <= arr[i] < 100
def countingSort(arr):
    result = []
    for i in range(100):
        result += [0]

    for i in range(len(arr)):
        result[arr[i]] += 1

    return result
# Link to challenge
# https://www.hackerrank.com/challenges/lisa-workbook/problem


def workbook(n, k, arr):
    page = 1
    count = 0

    for i in range(n):
        problem = 1
        while problem <= arr[i]:
            if problem == page:
                count += 1
            if problem % k == 0 or problem == arr[i]:
                page += 1
            problem += 1

    return count

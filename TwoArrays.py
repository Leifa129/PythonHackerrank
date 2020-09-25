# Link to challenge
# https://www.hackerrank.com/challenges/two-arrays/problem


def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"

    return "YES"
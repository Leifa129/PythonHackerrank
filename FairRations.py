# Link to challenge
# https://www.hackerrank.com/challenges/fair-rations/problem


def fairRations(B):
    count = 0
    if sum(B) % 2 != 0:
        return "NO"

    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            count += 2

    return count
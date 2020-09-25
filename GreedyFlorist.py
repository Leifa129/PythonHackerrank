# Link to challenge
# https://www.hackerrank.com/challenges/greedy-florist/problem


def getMinimumCost(k, c):
    c.sort()
    c.reverse()
    multiplier = 0
    friends = 0
    cost = 0
    for i in range(len(c)):
        if friends % k == 0:
            multiplier += 1
            friends = 0

        cost += c[i] * multiplier
        friends += 1

    return cost
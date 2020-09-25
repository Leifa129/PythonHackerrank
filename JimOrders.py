# Link to challenge
# https://www.hackerrank.com/challenges/jim-and-the-orders/problem


def jimOrders(orders):
    result = list(map(lambda x: x[0] + x[1], orders))
    temp = [i for i in range(1, len(orders) + 1)]
    easy = list(zip(result, temp))
    easy.sort()

    return map(lambda x: x[1], easy)
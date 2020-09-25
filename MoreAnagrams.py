# Link to challenge
# https://www.hackerrank.com/challenges/anagram/problem


def anagram(s):
    if len(s) % 2 != 0:
        return -1

    first = list(s[:len(s) // 2])
    second = list(s[len(s) // 2:])
    count = 0
    first.sort()
    second.sort()

    for i in first:
        if i not in second:
            count += 1

        else:
            second.remove(i)

    return count

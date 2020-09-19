# Link to challenge
# https://www.hackerrank.com/challenges/anagram/problem

def anagram(s):
    if(len(s) % 2 != 0):
        return -1

    first = list(s[:int(len(s) / 2)])
    second = list(s[int(len(s) / 2):])

    count = 0

    for ch in first:
        if ch in second:
            second.remove(ch)

    return len(second)
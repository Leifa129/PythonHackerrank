# Link to challenge
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

def beautifulBinaryString(b):
    count = 0
    i = 0
    while i < len(b) - 2:
        if b[i] == '0' and b[i + 1] == '1' and b[i + 2] == '0':
            count += 1
            i += 2

        i += 1

    return count
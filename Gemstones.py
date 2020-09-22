# Link to challenge
# https://www.hackerrank.com/challenges/gem-stones/problem

import string

# Complete the gemstones function below.
def gemstones(arr):
    count = 0
    hashMap = {}
    for char in string.ascii_lowercase:
        hashMap[char] = 0
        for i in range(len(arr)):
            if char in arr[i]:
                hashMap[char] += 1

        if hashMap[char] == len(arr):
            count += 1

    return count
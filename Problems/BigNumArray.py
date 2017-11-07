import math
import itertools

def get_digit(number, n):
    return number // 10**n % 10


def getPairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs


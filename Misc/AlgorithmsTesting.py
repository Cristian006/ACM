import itertools as it

lookup = [None]*100


def fib(n, table):
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]

fib(5, lookup)

''' Longest Increasing Subsequence '''
arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]


def longest_increasing_subseq(seq):
    num_increasing = [1] * len(seq)
    increasing_seq = []

    for i in range(len(seq)):
        j = 0
        while j < i:
            if arr[j] < arr[i]:
                if num_increasing[j] + 1 > num_increasing[i]:
                    num_increasing[i] = num_increasing[j] + 1
            j += 1

        if len(increasing_seq) == 0:
            increasing_seq.append((num_increasing[i], i))
        elif num_increasing[i] == increasing_seq[-1][0]:
            increasing_seq[-1] = (num_increasing[i], i)
        elif num_increasing[i] > increasing_seq[-1][0]:
            increasing_seq.append((num_increasing[i], i))

    return num_increasing, increasing_seq

# ints, seqs = longest_increasing_subseq(arr)
# print(seqs)
# print(ints)

# arr = [5, 6, 3, 5, 7, 8, 9, 120, 200, 1, 2]

def findingContiguousIncreasingSubSeq(arr):
    m = 1
    cur_max = m
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            cur_max += 1
        else:
            if cur_max > m:
                m = cur_max

            cur_max = 1

    if cur_max > m:
        cur_max = cur_max

    return m


"""
    1) there are always 2^n elements in the power set of a set; where n = size of set
    2) a power set of a set S is the set of ALL subsets of S including {} and S itself

    the below is the brute force approach to getting the longest common subsequence

    The idea is that if we have all possible combinations of sets for both S1 and S2
    we can then store all the sets that are common to both power sets, we can then take the
    one with the largest number of elements

    this is O(n * 2^n) time complexity  yea........
"""


def powerSet(arr):
    power_set = []
    size = len(arr)
    power_set_size = 2 ** size

    for counter in range(power_set_size):
        innerList = []
        for j in range(size):
            if counter & (1 << j):
                innerList.append(arr[j])
        power_set.append(innerList)

    return power_set


def longestIncreasingSubseq(seq1, seq2):
    pws1 = powerSet(seq1)
    pws2 = powerSet(seq2)

    equal_sets = []
    for ps1 in pws1:
        for ps2 in pws2:
            if ps1 == ps2:
                equal_sets.append(ps1)
                break

    return equal_sets[-1]


''' Longest Common Subsequence '''
# print(longestIncreasingSubseq(s1, s2))

"""
    Imagine we have two strings with even 30 chars in each. the above we take more than 32,212,254,720 
    to calculate only ONE of the powersets!!!! not even the other one  would take god knows how long but
    maybe even weeks. this is undoable

    Below is a better approach:
    L() --> longest common sub-sequence function name

    key 1: IF len(s1) == 0 OR len(s2) == 0 THEN --> L( s1, s2 ) = 0

    key 2: IF s1[-1] == s2[-1] THEN --> 1 + L( s1[:-2], s2[:-2] )
        * this means the last char matched and thus we now that we have a match;
            we just make a recursive call to L with the subsequence not including the last ones

    key 3: IF s1[-1] != s2[-1] THEN --> MAX( L(s1,s2[:-2]), L(s1[:-2], s2) )
        * meaning, if the last chars do not match, then we make a recursive call with the 
            two possible directions we can go

            ex:  say we have s1 = ADXD and s2 = ADDY  this shows why we do above

        we can NOT call MAX(L(s1, s2), L(s1, s2))  we have to somehow keep reducing the problem
"""

s1 = "AXBRZZII"
s2 = "ABAYBZIR"

# so so so much faster!!!
def LCSRecursive(seq1, seq2, i, j, lookup):
    if i == -1 or j == -1:
        return 0
    elif seq1[i] == seq2[j]:
        code = seq1[:i]+','+seq2[:j]
        if code in lookup:
            return 1 + lookup[code]
        else:
            lookup[code] = LCSRecursive(seq1, seq2, i-1, j-1, lookup)
            return 1 + lookup[code]
    else:
        left_code = seq1[:i+1]+','+seq2[:j]
        right_code = seq1[:i]+','+seq2[:j+1]
        if left_code not in lookup:
            lookup[left_code] = LCSRecursive(seq1, seq2, i, j-1, lookup)
        if right_code not in lookup:
            lookup[right_code] = LCSRecursive(seq1, seq2, i-1, j, lookup)

        return max(lookup[left_code], lookup[right_code])


# memoized version
def LCS(seq1, seq2):
    lookup = {}
    num = LCSRecursive(seq1, seq2, len(seq1)-1, len(seq2)-1, lookup)
    print(lookup)
    return num


def LongCS(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    L = [[None]*(n+1) for k in range(m+1)]

    for r in range(m+1):
        for c in range(n+1):
            if r == 0 or c == 0:
                L[r][c] = 0
            elif seq1[r-1] == seq2[c-1]:
                L[r][c] = L[r-1][c-1] + 1
            else:
                L[r][c] = max(L[r-1][c],L[r][c-1])

    sequence = []
    r = m
    c = n
    while r != 0 and c != 0:
        v = max(L[r-1][c], L[r][c-1])
        if L[r][c] != v:
            sequence.append((r-1, c-1))
            r -= 1
            c -= 1
        else:
            if v == L[r-1][c]:
                r = r-1
            else:
                c = c-1

    sequence.reverse()
    return sequence


# tabular approach to the Edit distance problem
def minEditDistance(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    # create a matrix with n+1 columns and m+1 rows; +1 because we need to include phi
    L = [[0]*(n+1) for i in range(m+1)]

    for r in range(m+1):
        for c in range(n+1):
            if r == 0:
                L[r][c] = c
            elif c == 0:
                L[r][c] = r
            elif seq1[r-1] == seq2[c-1]:
                L[r][c] = L[r-1][c-1]
            else:
                L[r][c] = 1 + min(L[r-1][c], L[r-1][c-1], L[r][c-1])

    return L[m][n]

"""
BARBELLS
"""

# the powerset
def PS(S, includeEmpty=False, includeFullSet = False):
    ps = []
    # n being the size of the combinations produced
    # itertools.combinations() returns all possible combinations of size n
    start = 1
    if includeEmpty:
        start = 0
    finish = len(S)
    if includeFullSet:
        finish += 1

    for n in range(start, finish):
        for c in it.combinations(S, n):
            ps.append(c)
    return ps


"""
    Write a program to print all permutations of a sequence;
    this one is a bit tricky:
    
    We know that the number of permutations is N!.
    Here is the key to understanding this algorithm with an example:
    What is all permutations of S = 'ABCD' ?
    well its, (All permutations starting with A) 
    + (all perms s.w. B) + (all perms s.w. C) +
    (all perms starting with D)
    
    Again, what are all permutations s.w. AB?
    well its: (all perms s.w. ABC) + (all perms s.w. ABD)
    
    KEY: 1) swap with L with I indices
         2) Call recursively
         3) undo-swaping
         4) increment i
         5) swap L index with I
         6) when l == r then record
"""
def swap(seq, a, b):
    temp = seq[a]
    seq[a] = seq[b]
    seq[b] = temp

def permute(sequence, l, r, perms):
    if l == r:
        perms.append(list(sequence))
    else:
        for i in range(l, r):
            swap(sequence, l, i)
            permute(sequence, l+1, r, perms)
            swap(sequence, l, i)

# perms = []
# seq = ["A", "B", "C", "D"]
# permute(seq, 1, len(seq), perms)
# print(perms)

"""
    What About All possible combinations?
    Print all possible combinations of r
    elements given an array of size n
    
    we need to try to understand this later
"""

def combinations(arr, n, r, index, i, data):
    if index == r:
        print(data)
        return

    if i >= n:
        return

    data[index] = arr[i]
    combinations(arr, n, r, index+1, i+1, data)
    combinations(arr, n, r, index, i + 1, data)


def printCombos(arr, r):
    data = [None] * r
    n = len(arr)
    combinations(arr, n, r, 0, 0, data)


s = ['a', 'b', 'c', 'd', 'e']
printCombos(s, 3)

# def explore(plates, bars, at, leftW, rightW, seen):
#     if at == len(plates):
#         print(leftW, rightW)
#         return
#
#     explore(plates, bars, at+1, leftW, rightW, seen)
#     explore(plates, bars, at+1, leftW+plates[at], rightW, seen)
#     explore(plates, bars, at+1, leftW, rightW + plates[at], seen)
#
# ws = [5, 5, 1, 4]
# brs = [100, 110]
# S = set([])
# explore(ws, brs, 0, 0, 0, S)


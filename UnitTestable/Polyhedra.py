# Submitted
a = int(input())

def convex(numOfInput):
    for i in range(numOfInput):
        v, e = input().split(" ")
        print(polyhedra(int(v), int(e)))

def polyhedra(vert, edge):
    return 2 - vert + edge

convex(a)
import sys

for _ in range(int(input())):
    hashmap = {}
    t = int(input())
    sum = t
    for i in range(t):
        x, y = sys.stdin.readline().split()
        if y in hashmap:
            hashmap[y] += 1
        else:
            hashmap[y] = 1
    case = 1
    for i in hashmap.keys():
        case *= hashmap[i] + 1
    print(case - 1)
import sys
from collections import deque

input = sys.stdin.readline

S = list(input().rstrip())

temp = []
temp.append(S[0])

for i in range(1, len(S)):
    if temp[0] >= S[i]:
        temp.reverse()
        temp.append(S[i])
        temp.reverse()
    else:
        temp.append(S[i])

print("".join(temp))
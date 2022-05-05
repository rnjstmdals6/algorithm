import sys
from collections import deque

input = sys.stdin.readline

S = list(input().rstrip())

temp = deque()
temp.append(S[0])

for i in range(1, len(S)):
    if temp[0] >= S[i]:
        temp.appendleft(S[i])
    else:
        temp.append(S[i])

print("".join(temp))
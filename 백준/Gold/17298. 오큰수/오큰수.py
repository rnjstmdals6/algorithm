import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
stack = []
result = []
for i in range(N-1, -1, -1):
    while stack:
        if S[i] < stack[-1]:
            result.append(stack[-1])
            stack.append(S[i])
            break
        else:
            stack.pop()
    if len(stack) == 0:
        result.append(-1)
        stack.append(S[i])
result.reverse()
print(*result)
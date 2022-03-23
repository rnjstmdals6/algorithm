import sys
from collections import deque
input = sys.stdin.readline

q = deque(list(input().rstrip()))
ans = []
s = len(q)
for i in range(s):
    ans.append(list(q))
    q.popleft()

res = []
for i in ans:
    string = ''
    for j in range(len(i)):
        string += i[j]
    res.append(string)

res.sort()

for i in res:
    print(i)
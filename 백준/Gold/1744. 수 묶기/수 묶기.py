import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s = []
s1 = []
for _ in range(N):
    a = int(input())
    if a > 0:
        s.append(a)
    else:
        s1.append(a)

s.sort(reverse = True)
s1.sort()

visited = [False] * len(s)
visited1 = [False] * len(s1)

ans = 0
# 양수부터
for i in range(len(s)-1):
    if visited[i]:
        continue
    if not visited[i] and not visited[i+1]:
        if (s[i] * s[i+1]) > (s[i] + s[i+1]):
            ans += (s[i] * s[i+1])
            visited[i], visited[i+1] = True, True
        else:
            ans += s[i]
            visited[i] = True

if len(s) > 0 and not visited[len(s)-1]:
    ans += s[len(s)-1]

# 음수 처리

for i in range(len(s1)-1):
    if visited1[i]:
        continue
    if not visited1[i] and not visited1[i+1]:
        if (s1[i] * s1[i+1]) > (s1[i] + s1[i+1]):
            ans += (s1[i] * s1[i+1])
            visited1[i], visited1[i+1] = True, True
        else:
            ans += s1[i]
            visited1[i] = True

if len(s1) > 0 and not visited1[len(s1)-1]:
    ans += s1[len(s1)-1]

print(ans)
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

n = int(input())
words = [list(map(lambda x:ord(x) - 65, input().rstrip())) for _ in range(n)]
alphabets = [0] * 26

for word in words:
    for idx, char in enumerate(word[::-1]):
        alphabets[char] += 10 ** idx

alphabets.sort(reverse=True)
ans = 0
key = 9
for i in range(9):
    ans += key * alphabets[i]
    key -= 1
print(ans)
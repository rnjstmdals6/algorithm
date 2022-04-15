N = int(input())
M = int(input())
ans = abs(N - 100)
if M:
    button = set(input().split())
else:
    button = set()

for num in range(1000001):
    for i in str(num):
        if i in button:
            break
    else:
        ans = min(ans, len(str(num))+abs(N - num))

print(ans)
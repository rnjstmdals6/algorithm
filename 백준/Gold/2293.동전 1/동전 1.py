n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

countList = [0] * (k + 1)
countList[0] = 1

for i in coins:
    for j in range(i, k + 1):
        countList[j] += countList[j - i]

print(countList[k])
import sys
# 끊어진 기타 줄 개수, 기타줄 브랜드 수
N, M = map(int, sys.stdin.readline().split())
# 패키지가격 낱개 가격
package = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

A = sorted(package, key=lambda x: x[0])
B = sorted(package, key=lambda x: x[1])

result = 0
a = A[0][0]
b = B[0][1]
while N > 5:
    if a < (b * 6):
        N -= 6
        result += a
    else:
        N -= 1
        result += b

if N > 0 and a < (b * N):
    result += a
else:
    result += (b * N)

print(result)
import sys
from collections import deque
sys.setrecursionlimit(100000)
INF = int(1e9)

if __name__ == "__main__":
    def power(adj, n):
        if n == 1:
            return adj
        else:
            x = power(adj, n // 2)
            if n % 2 == 1:
                return multi(multi(x, x), adj) # x * x * C
            else:
                return multi(x, x) # x * x

    def multi(m1, m2):
        temp = [[0] * len(m2) for _ in range(len(m2))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                sum = 0
                for k in range(len(m2)):
                    sum += m1[i][k] * m2[k][j]
                temp[i][j] = sum % 1000000007
        return temp

    adj = [[1, 1], [1, 0]]
    n = int(input())
    if n < 3:
        print(1)
    else:
        print(power(adj, n - 1)[0][0])

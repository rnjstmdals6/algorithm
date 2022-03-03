import sys
from collections import deque
sys.setrecursionlimit(100000)
INF = int(1e9)

if __name__ == "__main__":

    N = int(input()) // 3
    K = 0
    while 2 ** K != N:
        K += 1

    Astar = ["  *  ", " * * ", "*****"]

    def fun(star):
        M = len(star)

        for i in range(M):
            star.append(star[i] + " " + star[i])
            star[i] = " " * M + star[i] + " " * M
        return star

    for i in range(K):
        Astar = fun(Astar)

    for i in Astar:
        print(i)
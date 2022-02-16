import math
import sys
from collections import deque

INF = sys.maxsize

if __name__ == "__main__":
    n = list(input())

    result = 0
    i = 0

    while i < len(n):
        result += 1

        if i < len(n) - 1:
            if n[i] == "c":
                if n[i + 1] == "=":
                    i += 1
                elif n[i + 1] == "-":
                    i += 1
            elif n[i] == "d":
                if n[i + 1] == "-":
                    i += 1
                elif i < len(n) - 2:
                    if n[i + 1] == "z" and n[i + 2] == "=":
                        i += 2
            elif n[i] == "l" and n[i + 1] == "j":
                i += 1
            elif n[i] == "n" and n[i + 1] == "j":
                i += 1
            elif n[i] == "s" and n[i + 1] == "=":
                i += 1
            elif n[i] == "z" and n[i + 1] == "=":
                i += 1
        i += 1
    print(result)
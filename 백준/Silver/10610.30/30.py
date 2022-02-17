import sys
import re
from itertools import permutations

INF = sys.maxsize

if __name__ == "__main__":
    n = list(input())
    n.sort(reverse=True)
    result = re.sub(r'[^0-9]', '', str(n))

    if int(result) % 30 == 0:
        print(result)
    else:
        print(-1)
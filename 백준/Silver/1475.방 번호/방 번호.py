import copy
import sys
import re
from collections import deque
from itertools import permutations

INF = sys.maxsize

if __name__ == "__main__":
    n = list(input())
    pack = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pack2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cnt = 1


    for i in n:
        if i in pack:
            pack.remove(i)
        elif i == '6' and '9' in pack:
            pack.remove('9')
        elif i == '9' and '6' in pack:
            pack.remove('6')
        else:
            cnt += 1
            pack.extend(pack2)
            pack.remove(i)
    print(cnt)
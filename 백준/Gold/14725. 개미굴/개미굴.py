import copy
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.data = string

    def search(self, cur, level):
        if level == 0:
            cur = self.head
        for child in sorted(cur.children.keys()):
            print("--" * level, child, sep="")
            self.search(cur.children[child], level + 1)
        return True


N = int(input())
trie = Trie()

for k in range(N):
    data = list(input().split())
    trie.insert(data[1:])

trie.search(None, 0)

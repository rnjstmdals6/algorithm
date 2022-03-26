import heapq
import sys

INF = 1e9
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        cur_node = self.root

        for s in string:
            if s not in cur_node.children:
                cur_node.children[s] = Node(s)
            cur_node = cur_node.children[s]

        cur_node.data = string

    def search(self, string):
        cur_node = self.root

        for s in string:
            if s in cur_node.children:
                cur_node = cur_node.children[s]
            else:
                return False
        if cur_node.data:
            return True
        return False

N, M = map(int, input().split())
trie = Trie()
cnt = 0
for _ in range(N):
    string = input().rstrip()
    trie.insert(string)

for _ in range(M):
    string = input().rstrip()
    if trie.search(string):
        cnt += 1

print(cnt)

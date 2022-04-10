import sys

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

    def search(self, string):
        cur = self.head

        for char in string:
            if char in cur.children:
                cur = cur.children[char]
        if cur.children:
            return False
        return True


for _ in range(int(input())):
    n = int(input())
    arr = [(input().rstrip()) for i in range(n)]
    arr.sort()
    trie = Trie()

    for string in arr:
        trie.insert(string)

    flag = True

    for k in arr:
        if not trie.search(k):
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')
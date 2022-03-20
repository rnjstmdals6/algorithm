import sys
input = sys.stdin.readline

def dfs(v):
    global cnt
    if len(tree[v]) == 0:
        cnt += 1
        return
    for i in tree[v]:
        dfs(i)

N = int(input())
parent = list(map(int, input().split()))
tree = [[] for _ in range(N)]
start = 0
cnt = 0

for i in range(len(parent)):
    if parent[i] != -1:
        tree[parent[i]].append(i)
    else:
        start = i
delete = int(input())
if parent[delete] == -1:
    print(0)
else:
    tree[delete].clear()
    tree[parent[delete]].remove(delete)
    dfs(start)
    print(cnt)
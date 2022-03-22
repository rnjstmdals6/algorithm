import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [[0] * 3 for _ in range(4)]


# 남쪽으로 굴리기
def south():
    temp = dice[3][1]

    for i in range(3, -1, -1):
        dice[i][1] = dice[i - 1][1]

    dice[0][1] = temp


# 북쪽으로 굴리기
def north():
    temp = dice[0][1]

    for i in range(1, 4):
        dice[i - 1][1] = dice[i][1]

    dice[3][1] = temp


# 서쪽으로 굴리기
def west():
    up = dice[1][1]
    right = dice[1][2]
    left = dice[1][0]
    down = dice[3][1]

    dice[1][0] = up
    dice[3][1] = left
    dice[1][2] = down
    dice[1][1] = right

# 동쪽으로 굴리기
def east():
    up = dice[1][1]
    right = dice[1][2]
    left = dice[1][0]
    down = dice[3][1]

    dice[1][2] = up
    dice[3][1] = right
    dice[1][0] = down
    dice[1][1] = left


for command in commands:
    if command == 1:
        if 0 <= y + 1 < M:
            east()
            y += 1
        else:
            continue
    elif command == 2:
        if 0 <= y - 1 < M:
            west()
            y -= 1
        else:
            continue
    elif command == 3:
        if 0 <= x - 1 < N:
            north()
            x -= 1
        else:
            continue
    elif command == 4:
        if 0 <= x + 1 < N:
            south()
            x += 1
        else:
            continue
    if graph[x][y] == 0:
        graph[x][y] = dice[3][1]
    else:
        dice[3][1] = graph[x][y]
        graph[x][y] = 0
    print(dice[1][1])

from collections import deque


Q = deque()
dr = [-1,0,1,0]
dc = [0,1,0,-1]

M,N = map(int,input().split())
dist = [[0]*M for _ in range(N)]

tomato = [list(map(int,input().split())) for _ in range(N)]

def BFS():
    global cnt
    while Q:
        r, c = Q.popleft()
        tomato[r][c] = -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr <0 or nr >=N or nc < 0 or nc >= M:
                continue
            if tomato[nr][nc] == -1 or dist[nr][nc] != 0:
                continue
            if tomato[nr][nc] == 1:
                continue
            Q.append((nr,nc))
            dist[nr][nc] = dist[r][c] + 1
            cnt = dist[nr][nc]


for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append((i,j))


cnt = 0
BFS()

flag = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            flag = 1
            cnt = -1
            break
    if flag == 1:
        break

print(cnt)

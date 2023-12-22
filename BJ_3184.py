import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)

dr = [-1,0,1,0]
dc = [0,1,0,-1]

R,C = map(int, input().split())

area1 = [list(input()) for _ in range(R)]

def DFS(r,c):
    global ww,ss
    if area1[r][c] == 'o':
        ss += 1
    if area1[r][c] == 'v':
        ww += 1
    area1[r][c] = '#'
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if area1[nr][nc] == '#':
            continue
        DFS(nr,nc)



wolf = 0
sheep = 0

for i in range(R):
    for j in range(C):
        if area1[i][j] != '#':
            ww = 0
            ss = 0
            DFS(i,j)
            if ww < ss:
                sheep += ss
            else:
                wolf += ww

print(sheep,wolf)
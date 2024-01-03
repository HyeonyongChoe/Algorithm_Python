T = int(input())

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def DFS(r,c):
    global ans
    mase[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if mase[nr][nc] == 1:
            continue
        if mase[nr][nc] == 3:
            ans = 1
            return
        DFS(nr,nc)

for i in range(1,T+1):
    N = int(input())
    mase = [list(map(int,input())) for _ in range(N)]
    for ii in range(N):
        for jj in range(N):
            if mase[ii][jj]==2:
                ans = 0
                DFS(ii,jj)
                print(f"#{i} {ans}")


#
from collections import deque

T = int(input())

direc_dic = {1:[0,1,2,3], 2:[0,2], 3:[1,3], 4:[0,1], 5:[1,2], 6:[2,3], 7:[3,0]}
dr = [-1,0,1,0]
dc = [0,1,0,-1]



def bfs():
    global cnt
    time = 1

    while time < L:
        for t in range(len(Q)):
            r, c = Q.popleft()
            chk[r][c] = 1
            if underworld[r][c] == 0:
                continue
            for i in direc_dic[underworld[r][c]]:
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= M or underworld[nr][nc] == 0 or chk[nr][nc] == 1:
                    continue
                if (i+2)%4 in direc_dic[underworld[nr][nc]] and chk[nr][nc] == 0:
                    chk[nr][nc] = 1
                    Q.append((nr,nc))
                    cnt += 1
                    underworld[r][c] = 0
        time += 1
        if time == L:
            break


for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    underworld = [list(map(int,input().split())) for _ in range(N)]
    chk = [[0]*M for _ in range(N)]
    Q = deque()
    Q.append((R,C))
    cnt = 1
    bfs()
    print(f"#{tc} {cnt}")




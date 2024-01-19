from collections import deque

T = int(input())

def dfs(n,x,y,tot):
    global ans
    if n == N:
        tot += abs(x-d_x) + abs(y-d_y)
        ans = min(tot,ans)
        return

    if tot > ans:
        return

    for i in range(0,N):
        if chk[i] == 1:
            continue
        if chk[i] == 0:
            chk[i] = 1
            xx = arr1[2*i]
            yy = arr1[2*i+1]
            tot += abs(x - xx) + abs(y - yy)
            dfs(n+1,xx,yy,tot)
            tot -= abs(x - xx) + abs(y - yy)
            chk[i] = 0


for ts in range(1,T+1):
    N = int(input())
    Q = deque(list(map(int,input().split())))
    chk = [0]*N
    s_x = Q.popleft()
    s_y = Q.popleft()
    d_x = Q.popleft()
    d_y = Q.popleft()
    arr1 = list(Q)
    ans = 999999999
    dfs(0,s_x,s_y,0)
    print(f"#{ts} {ans}")

N, M = map(int,input().split())

city = [list(map(int,input().split())) for _ in range(N)]

home = []
chick_seller = []


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i,j])
        if city[i][j] == 2:
            chick_seller.append([i,j])

chick_dis = []
for i in range(len(chick_seller)):
    chick_dis.append([])
    for j in range(len(home)):
        chick_dis[i].append(abs(chick_seller[i][0]-home[j][0])+abs(chick_seller[i][1]-home[j][1]))

chk = [0]*len(chick_seller)

chk_pt = []
def find_dis(n,idx):
    global ans
    if n == M:
        sel_dis = [101] * len(home)
        for i in chk_pt :
            for j in range(len(sel_dis)):
                sel_dis[j] = min(sel_dis[j], chick_dis[i][j])
        tot = sum(sel_dis)
        ans = min(ans,tot)
        return

    for i in range(idx,len(chick_seller)):
        if chk[i] == 1:
            continue
        if chk[i] == 0:
            chk[i] = 1
            chk_pt.append(i)
            find_dis(n+1,i)
            chk[i] = 0
            chk_pt.pop()

ans = 999999999

find_dis(0,0)

print(ans)
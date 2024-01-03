N, M = map(int,input().split())

arr1 = list(map(int,input().split()))

sel = [0]* M
chk = [0]* N
ans = []
def permu(n):
    if n == M:
        ans.append(sel[:])
        return

    for i in range(N):
        if chk[i] != 1 :
            chk[i] = 1
            sel[n] = arr1[i]
            permu(n+1)
            chk[i] = 0

permu(0)

ans = sorted(ans,key=lambda x : x)

for i in ans:
    print(*i)


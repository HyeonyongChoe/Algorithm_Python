N, M = map(int,input().split())

arr1 = sorted(list(map(int,input().split())))

sel = [0]*M

def combi(idx, sidx):
    if sidx == M:
        print(*sel)
        return

    if idx == N:
        return

    sel[sidx] = arr1[idx]
    combi(idx+1,sidx+1)
    combi(idx+1,sidx)

combi(0,0)

#


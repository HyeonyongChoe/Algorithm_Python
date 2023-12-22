arr1 = [list(map(int,input().split())) for _ in range(5)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def DFS(r,c,s):
    word = s+str(arr1[r][c])
    if len(word) == 6:
        set1.add(word)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >=5 or nc < 0 or nc >=5:
                continue
            DFS(nr,nc,word)

set1=set()

for i in range(5):
    for j in range(5):
        DFS(i,j,'')

print(len(set1))
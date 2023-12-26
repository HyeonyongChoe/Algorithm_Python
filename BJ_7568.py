N = int(input())

data1 = [list(map(int,input().split())) for _ in range(N)]

grade1 = [1]*N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if data1[i][0] < data1[j][0] and data1[i][1] < data1[j][1]:
            grade1[i] += 1

print(*grade1)
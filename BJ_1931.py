N = int(input())

meeting = []

for _ in range(N):
    meeting.append(list(map(int,input().split())))

meeting = sorted(meeting, key=lambda x : (x[1],x[0]))

cnt = 0
standard = -1
for i in meeting:
    if i[0] >= standard :
        cnt += 1
        standard = i[1]

    else :
        continue

print(cnt)
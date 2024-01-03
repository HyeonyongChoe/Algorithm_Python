N, Q = map(int,input().split())

USADO = [[0]*(N+1) for _ in range(N+1)]

for i in range(N-1):
    p,q,r = map(int,input().split())
    USADO[p][q] = r

#for i in range(Q):
#    k, v = map(int,input().split())
#    for j in range(1,N+1):
# 값
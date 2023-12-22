N = int(input())

if N == 1:
    print(1)

else:

    cnt = 0
    while N > 2**cnt:
        cnt += 1

    cnt1 = 1
    for i in range(int(2**(cnt-1)+1),N+1):
        if i == N:
            print(2*cnt1)
            break
        else:
            cnt1 += 1


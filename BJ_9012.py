T = int(input())

for i in range(T):
    PS = list(input())
    standard = 0
    for j in PS:
        if j == '(':
            standard += 1
        elif j == ')':
            standard -= 1
        if standard < 0 :
            break

    if standard == 0:
        print("YES")
    else :
        print("NO")


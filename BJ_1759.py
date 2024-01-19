L, C = map(int,input().split())

arr1 = sorted(list(input().split()))

chk = [0]*C
word = []
vowel_chk = 0
else_chk = 0
def permu(n,idx):
    global vowel_chk, else_chk
    if n == L and vowel_chk >= 1 and else_chk >= 2:
        ans = ''.join(word)
        print(ans)
        return

    for i in range(idx,C):
        if chk[i] == 1:
            continue
        if chk[i] == 0:
            chk[i] = 1
            if arr1[i] in 'aeiou':
                vowel_chk += 1
            else:
                else_chk += 1
            word.append(arr1[i])
            permu(n+1,i+1)
            if arr1[i] in 'aeiou':
                vowel_chk -= 1
            else:
                else_chk -= 1
            word.pop()
            chk[i] = 0


permu(0,0)
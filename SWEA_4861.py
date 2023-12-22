T = int(input())

def palindrome_finder(arr1):
    for i in arr1:
        for j in range(N-M+1):
            worda = i[j:j+M]
            if worda == worda[::-1]:
                return worda
    return ''

for i in range(1,T+1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    if palindrome_finder(words):
        answer = ''.join(palindrome_finder(words))
        print(f"#{i} {answer}")
        continue

    transposed_words = list(zip(*words))
    if palindrome_finder(transposed_words):
        answer = ''.join(palindrome_finder(transposed_words))
        print(f"#{i} {answer}")


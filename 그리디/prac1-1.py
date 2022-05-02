#큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #작은 순서부터 큰 순서로 정렬
first = data[n-1]
second = data[n-2]

sum = 0

while True:
    for i in range(k): #k번 더하기
        if m == 0: #더하는 횟수가 0이라면 탈출
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1

print(sum)
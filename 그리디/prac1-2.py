#숫자 카드 게임

result = []
n, m = map(int, input().split())
for i in range(0, n):
    num = list(map(int, input().split()))
    minNum = min(num) #행 내의 최소 숫자 찾기
    result.append(minNum)

print(max(result))
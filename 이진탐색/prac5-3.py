## 실전문제3: 떡볶이 떡 만들기
#교재 참고. 파라메트릭 서치 문제는 이진 탐색을 재귀가 아닌 반복문으로 구현하면 쉬움!

n, m = map(int, input().split())
arr = list(map(int, input().split()))

#재귀로 풀려했으나 반복문이 더 간단하다는 힌트를 보고 변경
start = 0
end = max(arr) #최대 길이

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid: #자를 길이보다 크면
            total += i-mid 
    if total < m:
        end = m-1
    else:
        result = mid #임시 기록. "최대한"이니까
        start = m+1

print(result)
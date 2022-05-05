## 실전문제 3: 두 배열의 원소 교체

#배열 A에서는 가장 작은 것 K개, 배열 B에서는 가장 큰 것 K개 골라야 함.
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#바꿔치기 연산
a.sort()
b.sort(); b.reverse() # = b.sort(reverse=True)로 가능
for i in range(k): #K번 바꾸기
    a[i], b[i] = b[i], a[i]

print(sum(a))
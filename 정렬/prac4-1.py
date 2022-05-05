## 실전문제 1: 위에서 아래로

#계수 정렬 사용해봄
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

count = [0] * (max(arr)+1)
for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)-1, 0, -1): #역순 출력
    for j in range(count[i]):
        print(i, end=' ')


#정렬 라이브러리 사용 (책의 해설)
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)
for i in arr:
    print(i, end=" ")
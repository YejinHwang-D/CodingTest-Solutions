## 실전문제 2: 성적이 낮은 순서로 학생 출력하기

#성적=계수정렬
def setting(data):
    return data[1]

n = int(input())
arr = []
for i in range(n):
    info = input().split()
    arr.append((info[0], int(info[1])))

result = sorted(arr, key=lambda x : x[1])
for i in arr:
    print(i[0], end=' ')
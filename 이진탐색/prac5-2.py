## 실전문제2: 부품 찾기

n = int(input())
store = list(map(int, input().split()))
m = int(input())
custom = list(map(int, input().split()))

store.sort()


def search(arr, target, start, end):
    if start > end:
        return False
    mid = (end + start) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return search(arr, target, start, mid-1)
    else:
        return search(arr, target, mid+1, end)


for i in custom:
    result = search(store, i, 0, n-1)
    if result == False:
        print('no', end=" ")
    else:
        print('yes', end=" ")
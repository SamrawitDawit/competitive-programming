n, k = tuple(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
arr.sort()
if k==0:
    if arr[0]>1:
        print(arr[0]-1)
    else:
        print(-1)
elif k==n:
    print(arr[k-1])
elif arr[k-1] == arr[k]:
    print(-1)
else:
    print(arr[k-1])

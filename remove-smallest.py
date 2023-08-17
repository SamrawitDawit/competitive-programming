t = int(input())
for test_case in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr = sorted(arr)
    new_arr = []
    for ind in range(n-1):
        if arr[ind+1] -arr[ind] <= 1:
            new_arr.append(min(arr[ind +1], arr[ind]))
    if n - len(new_arr) == 1:
        print("YES")
    else:
        print("NO")

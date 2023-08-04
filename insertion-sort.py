def insertionSort1(n, arr):
    # Write your code here
    if n == 1:
        print(arr[0])
    else: 
        temp = arr[-1]
        for i in range(-2,-n-1,-1):
            if arr[i] < temp:
                arr[i+1] = temp
                print(*arr, end='\n')
                break
            else:
                arr[i+1] = arr[i]
                print(*arr, end='\n')
        if temp < arr[0]:
            arr[0] = temp
            print(*arr)

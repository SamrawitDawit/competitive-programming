def countingSort(arr):
    freq_arr = [0]*100
    for i in arr:
        freq_arr[i] += 1
    return freq_arr

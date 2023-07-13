#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swap = 0
    for i in range(n-1):
        for j in range(1, n-i):
            if a[j-1] > a[j]:
                (a[j-1], a[j]) = (a[j], a[j-1])   
                swap += 1  
        if swap == 0:
            break
    print(f'Array is sorted in {swap} swaps.', end = "\n")
    print(f'First Element: {a[0]}', end = "\n")  
    print(f'Last Element: {a[-1]}', end = "\n") 
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

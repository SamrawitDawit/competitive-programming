def swap_case(s):
    swapped = ''
    for i in s:      
        if i == i.lower():
            swapped += i.upper()
        else:
            swapped += i.lower()
    return swapped 
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

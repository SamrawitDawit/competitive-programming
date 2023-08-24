class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lst = []
        i = 0
        while i*i <= c:
            lst.append(i*i)
            i += 1
        left = 0
        right = len(lst)-1
        while lst[left] + lst[right] != c and left < right:
            if lst[left] + lst[right] < c:
                left += 1
            elif lst[left] + lst[right] > c:
                right -= 1
        if lst[left] + lst[right] == c:
            return True
        return False

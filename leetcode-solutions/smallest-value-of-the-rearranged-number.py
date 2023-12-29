class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        s = str(num)
        s = list(s)
        if num > 0:
            s.sort()
            i, j = 0, 0
            while s[j] == '0':
                j += 1
            s[i], s[j] = s[j], s[i]
            print(s)
            return int(''.join(s))
        else:
            magnitude = sorted(s[1:], reverse = True)
            magnitude = int(''.join(magnitude))
            print(magnitude)
            return (0-magnitude)

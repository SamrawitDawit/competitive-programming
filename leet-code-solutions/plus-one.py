class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = len(digits)-2
            digits[-1] = 0
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                    i -= 1
                else:
                    digits[i] += 1
                    return digits
            if i == -1:
                return ([1] + digits)
        else:
            digits[-1] += 1
            return digits
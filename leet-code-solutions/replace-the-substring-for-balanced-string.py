class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        ans = 1000000000
        dist = n//4
        counter = collections.Counter(s)
        for value in counter.values():
            if value != dist:
                break
        else:
            return 0
        l, r = 0, 0
        allLessOrEqual = False
        while r < n:
            while allLessOrEqual == False and r < n:
                counter[s[r]] -= 1
                r += 1
                for value in counter.values():
                    if value > dist:
                        break
                else:
                    allLessOrEqual = True
            while l<= r and allLessOrEqual == True:
                counter[s[l]] += 1
                l += 1
                for value in counter.values():
                    if value > dist:
                        ans = min(ans, r-l+1)
                        allLessOrEqual = False
                        break
        return ans



class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = collections.defaultdict(int)
        max_f, l, summ = 0, 0, 0
        for i in range(len(fruits)):
            dic[fruits[i]] += 1
            summ += 1
            while len(dic) > 2:
                dic[fruits[l]] -= 1
                summ -= 1
                if not dic[fruits[l]]:
                    dic.pop(fruits[l])
                l += 1
            max_f = max(max_f, summ)
        return max_f





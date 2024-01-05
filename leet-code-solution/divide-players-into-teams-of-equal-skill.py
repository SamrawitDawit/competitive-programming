class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 1
        r = len(skill)-2
        summ = skill[0] + skill[len(skill)-1]
        product = skill[0]*skill[len(skill)-1]
        while l < r:
            if skill[l] + skill[r] == summ:
                product += (skill[l]*skill[r])
                l += 1
                r -= 1
            else:
                return -1
        return product
            
            

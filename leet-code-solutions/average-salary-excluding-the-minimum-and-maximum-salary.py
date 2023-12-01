class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        summ = sum(salary[1:-1])
        return (summ/(len(salary)-2))
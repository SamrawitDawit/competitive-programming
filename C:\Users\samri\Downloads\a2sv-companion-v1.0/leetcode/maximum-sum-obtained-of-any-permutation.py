class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq_indices = [0]*len(nums)
        for request in requests:
            freq_indices[request[0]] += 1
            if request[1] < len(nums)-1:
                freq_indices[request[1]+1] -= 1
        prefix = 0
        for i in range(len(nums)):
            prefix += freq_indices[i]
            freq_indices[i] = prefix
        return sum(num * freq for num, freq in zip(sorted(nums), sorted(freq_indices))) % (10 ** 9 + 7)
        
     
        

            
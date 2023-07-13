class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num_list = []
        for i in nums:
            num_list.append(int(i))
        num_list = list(reversed(sorted(num_list)))
        return str(num_list[k-1])

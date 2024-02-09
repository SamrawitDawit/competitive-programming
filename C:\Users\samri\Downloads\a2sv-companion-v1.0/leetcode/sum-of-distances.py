from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        freq_dic = defaultdict(int)
        indx_dic = defaultdict(list)
        prefix_dic = defaultdict(list)
        for i in range(len(nums)):
            freq_dic[nums[i]] += 1
            indx_dic[nums[i]].append(i)
            prefix_dic[nums[i]].append(i) if nums[i] not in prefix_dic else prefix_dic[nums[i]].append(i+prefix_dic[nums[i]][-1])
        for key in prefix_dic:
            prefixArray = prefix_dic[key]
            indices = indx_dic[key]
            occ = freq_dic[key]
            n = len(indices)
            for i in range(n):
                prefix = 0 if i == 0 else (indices[i]*(i))-prefixArray[i-1]
                suffix = 0 if i == n-1 else (prefixArray[-1]-prefixArray[i])-((occ-i-1)*indices[i])
                output[indx_dic[key][i]] = prefix + suffix
        return output
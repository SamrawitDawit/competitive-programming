class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*(len(temperatures))
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_ind, stack_t =  stack.pop()
                ans[stack_ind] = (i-stack_ind)
            stack.append([i,t])
        return ans
            
      
       
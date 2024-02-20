class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # stack = []
        # span = []
        # n = len(arr)
        # for i in range(n):
        #     lastPopped = i
        #     while stack and stack[-1][0] >= arr[i]:
        #         stack[-1][1][1] = i-1
        #         lastPopped = stack[-1][1][0]
        #         span.append(stack.pop())
        #     stack.append([arr[i], [lastPopped, n-1]])
        # span.extend(stack)
        # print(stack)
        # print(span)
        # return sum(span[i][0]*(span[i][1][1] - span[i][1][0] + 1) for i in range(n))%(10**9 + 7)
        forwardStack = [(0, -1)]
        backwardStack = [(0, len(arr))]
        prefix = [0]*len(arr)
        suffix = [0]*len(arr)
        for i in range(len(arr)):
            while forwardStack[-1][0] >= arr[i]:
                forwardStack.pop()
            prefix[i] = i-forwardStack[-1][1]
            forwardStack.append((arr[i], i))
        for i in range(len(arr)-1, -1, -1):
            while backwardStack[-1][0] > arr[i]:
                backwardStack.pop()
            suffix[i] = backwardStack[-1][1]-i
            backwardStack.append((arr[i], i))
        total = [0]*len(arr)
        for i in range(len(arr)):
            total[i] = prefix[i] * suffix[i]
        return sum(arr[i]*total[i] for i in range(len(arr)))%(10**9 + 7)

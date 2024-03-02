class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        l, r = 1, 2**(n-1)
        for i in range(n-1):
            mid =(l+r)//2
            if k > mid:
                l = mid+1
                curr = 0 if curr else 1 
                
            else:
                r = mid
        return curr

        # curr=0

        # left,right=1,2**(n-1)

        # for i in range(n-1):
        #     mid=(left+right)//2
        #     if k>mid:
        #         left=mid+1
        #         curr=abs(curr-1)
        #     else:
        #         right=mid
        # return curr
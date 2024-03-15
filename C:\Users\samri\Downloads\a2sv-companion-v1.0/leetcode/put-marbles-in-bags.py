class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_sum = []
        for i in range(len(weights)-1):
            pair_sum.append(weights[i] + weights[i+1])
        pair_sum.sort()
        return sum(pair_sum[len(pair_sum)-k+1:]) - sum(pair_sum[: k-1])
        #  if we do all possible combinations, we will notice a pattern that each score is the
        # sum of the two last elements of the weight and the sum of the other elements at the other
        #  boundaries of each pair. we need k-1 pairs because when the weight is distributed to k bags,
        #  it will have k-1 internal boundary pairs(end of one pair, start of the next pair)
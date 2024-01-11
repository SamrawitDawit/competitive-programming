class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r, res, count, count_w = 0, 0, float('inf'), 0, 0
        for r in range(len(blocks)):
            count += 1
            if blocks[r] == 'W':
                count_w += 1
            if count == k:
                res = min(count_w, res)
                count -= 1
                if blocks[l] == 'W':
                    count_w -= 1
                l += 1
        return res

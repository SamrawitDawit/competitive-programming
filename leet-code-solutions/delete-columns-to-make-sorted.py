class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        deleted = []
        for i in range(1, len(strs)):
            for j in range(len(strs[i])):
                if j not in deleted:
                    if strs[i][j] < strs[i-1][j]:
                        delete += 1
                        deleted.append(j)
        return delete
                
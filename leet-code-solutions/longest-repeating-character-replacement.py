class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        counter = collections.Counter()
        for i in range(len(s)):
            counter[s[i]] += 1
            max_count = max(max_count, counter[s[i]])
            if max_len - max_count >= k:
                counter[s[i-max_len]] -= 1
            else:
                max_len += 1
        return max_len


            

        
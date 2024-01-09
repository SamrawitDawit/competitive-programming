class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        len_window = 0
        frequent = 0
        counter = collections.Counter()
        for i in range(len(answerKey)):
            counter[answerKey[i]] += 1
            frequent = max(counter[answerKey[i]], frequent) 
            if len_window - frequent >= k:
                counter[answerKey[i-len_window]] -= 1
            else:
                len_window += 1
        return len_window



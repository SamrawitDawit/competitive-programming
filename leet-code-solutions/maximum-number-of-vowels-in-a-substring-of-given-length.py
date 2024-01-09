class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count_vowel = 0
        for letter in s[:k]:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                count_vowel += 1
        maximum = count_vowel
        for i in range(k,len(s)):
            if s[i-k] in ['a', 'e', 'i', 'o', 'u']:
                count_vowel -= 1
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                count_vowel += 1
            maximum = max(maximum, count_vowel)
        return maximum
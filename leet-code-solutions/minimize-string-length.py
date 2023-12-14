class Solution:
    def minimizedStringLength(self, s: str) -> int:
        unique_chars = {}
        for letter in s:
            unique_chars[letter] = 1
        return len(unique_chars)

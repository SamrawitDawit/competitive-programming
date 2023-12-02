class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        temp_word = strs[0]
        for word in strs[1:]:
            i = 0
            while i < min(len(word), len(temp_word)) and word[i] == temp_word[i]:
                output += word[i]
                i += 1
            temp_word = output
            output = ''
        return temp_word

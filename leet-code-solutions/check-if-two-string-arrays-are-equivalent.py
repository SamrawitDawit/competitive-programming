class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1Sum = word2Sum =''
        for word in word1:
            word1Sum += word
        for word in word2:
            word2Sum += word
        return(word1Sum == word2Sum)
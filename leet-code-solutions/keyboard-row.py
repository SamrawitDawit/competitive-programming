class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        keyboard1 = "qwertyuiop"
        keyboard2 = "asdfghjkl"
        keyboard3 =  "zxcvbnm"
        for word in words:
            if word[0].lower() in keyboard1:
                row = keyboard1
            elif word[0].lower() in keyboard2:
                row = keyboard2
            else:
                row = keyboard3
            for letter in word[1:]:
                letter = letter.lower()
                if letter not in row:
                    break
            else:
                output.append(word)
        return output

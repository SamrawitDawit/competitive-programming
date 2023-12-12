class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        s = s.split(' ')
        for i in range(len(s)-1 , -1, -1):
            if s[i] == '':
                continue
            print(s[i])
            lst.append(s[i].strip())
        return ' '.join(lst)

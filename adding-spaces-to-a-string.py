class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string_list = list(s)
        new_string = ''
        for i in spaces:
            string_list[i] = " "+s[i]
        for i in string_list:
            new_string += i
        del string_list
        return new_string

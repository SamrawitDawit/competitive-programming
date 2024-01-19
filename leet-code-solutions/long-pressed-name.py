class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0] or name[-1] != typed[-1] or len(name) > len(typed):
            return False
        ptr1, ptr2 = 0, 0
        while ptr1 < len(name) and ptr2 < len(typed):
            if name[ptr1] == typed[ptr2]:
                ptr1 += 1
                ptr2 += 1
            elif ptr1 > 0 and typed[ptr2] == name[ptr1-1]:
                while ptr2 < len(typed) and typed[ptr2] == name[ptr1-1]:
                    ptr2 += 1
            else:
                
                return False
        if ptr1 < len(name):
            return False
        if ptr2 < len(typed):
            if typed[ptr2] == name[-1]:
                while ptr2 < len(typed) and typed[ptr2] == name[-1]:
                    ptr2 += 1
                if ptr2 < len(typed):
                    return False
            else:
                return False
        return True

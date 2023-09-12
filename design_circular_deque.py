class MyCircularDeque:

    def __init__(self, k: int):
        self.lst = []
        self.k = k
    def insertFront(self, value: int) -> bool:
        if len(self.lst) == self.k:
            return False
        self.lst = [value] + self.lst
        return True
    def insertLast(self, value: int) -> bool:
        if len(self.lst) == self.k:
            return False
        self.lst.append(value)
        return True
    def deleteFront(self) -> bool:
        if len(self.lst) == 0:
            return False
        self.lst.pop(0)
        return True
    def deleteLast(self) -> bool:
        if len(self.lst) == 0:
            return False
        self.lst.pop()
        return True
    def getFront(self) -> int:
        if len(self.lst) == 0:
            return -1
        return self.lst[0]
    def getRear(self) -> int:
        if len(self.lst) == 0:
            return -1
        return self.lst[-1]
    def isEmpty(self) -> bool:
        return len(self.lst) == 0
    def isFull(self) -> bool:
        return len(self.lst) == self.k

def __init__(self, value: int, k: int):
        self.lst =[]
        self.k = k
        self.value = value
        self.length = 0
    def consec(self, num: int) -> bool:
        self.lst.append(num)
        if num != self.value:
            self.length = 0
            return False
        if num == self.value:
            self.length += 1
            if self.length < self.k:
                return False
            return True

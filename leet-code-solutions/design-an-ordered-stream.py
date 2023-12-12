class OrderedStream:

    def __init__(self, n: int):
        self.all=[0]*n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        chunks = []
        self.all[idKey-1] = value
        while self.ptr<len(self.all) and self.all[self.ptr] != 0:
            chunks.append(self.all[self.ptr])
            self.ptr += 1
        return chunks

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
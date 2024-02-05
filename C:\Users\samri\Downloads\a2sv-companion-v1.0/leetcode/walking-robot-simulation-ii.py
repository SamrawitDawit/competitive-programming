class Robot:

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.dic, i= {}, 0
        for w in range(self.width):
            self.dic[i] = (w, 0)
            i += 1
        for h in range(1,self.height):
            self.dic[i] = (w, h)
            i += 1
        for ww in range(1,self.width):
            self.dic[i] = (w-ww, h)
            i += 1
        for hh in range(1,self.height):
            self.dic[i] = (0, h-hh)
            i+= 1
        self.curr = 0
    def step(self, num: int) -> None:
        self.curr += num
    def getPos(self) -> List[int]:
        return self.dic[(self.curr % (2*((self.width+self.height)-2)))]
    def getDir(self) -> str:
        if self.curr == 0:
            return "East"
        position = self.getPos()
        if position[1] == 0 and position[0] != 0:
            return "East"
        elif position[0] == self.width-1:
            return "North"
        elif position[1] == self.height-1:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
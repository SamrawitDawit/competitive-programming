class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.dic = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.thisTime = currentTime
        if tokenId in self.dic and self.dic[tokenId] + self.timeToLive > self.thisTime:
            self.dic[tokenId] = self.thisTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.dic:
            if self.dic[token] + self.timeToLive > currentTime:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.q = deque([])
        self.hmap = {}
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hmap[tokenId] = self.hmap.get(tokenId,0)+1
        self.q.append((tokenId,currentTime+self.ttl))

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.sync(currentTime)
        if tokenId in self.hmap:
            self.hmap[tokenId] = self.hmap.get(tokenId,0)+1
            self.q.append((tokenId,currentTime+self.ttl))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.sync(currentTime)
        return len(self.hmap)
    
    def sync(self,currentTime):
        while self.q and self.q[0][1]<=currentTime:
            out = self.q.popleft()[0]
            self.hmap[out]-=1
            if self.hmap[out]==0:
                del self.hmap[out]
            
        

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
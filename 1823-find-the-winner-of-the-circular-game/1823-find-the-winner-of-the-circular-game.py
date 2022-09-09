class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x=0
        for i in range(1,n+1):
            x=(x+k)%i
        return x+1
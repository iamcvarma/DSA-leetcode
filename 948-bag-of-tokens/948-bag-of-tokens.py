class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i,j = 0,len(tokens)-1
        tokens = sorted(tokens)
        ma,curr=0,0
        while i<=j:
            if tokens[i]<=power:
                power-=tokens[i]
                i+=1
                curr+=1
                ma=max(ma,curr)
            elif curr>0:
                curr-=1
                power+=tokens[j]
                j-=1
            else:
                break
        return ma
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(i,ans,res):
            if i==n:
                res.append(''.join(map(str,ans)))
                return res
            if not ans:
                for j in range(1,10):
                    ans.append(j)
                    backtrack(i+1,ans,res)
                    ans.pop()
            else:
                for a in {ans[-1]+k,ans[-1]-k}:
                    if -1<a<10:
                        ans.append(a)
                        backtrack(i+1,ans,res)
                        ans.pop()
            return res
        return backtrack(0,[],[])
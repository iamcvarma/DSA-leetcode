class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        st,res=[inf],0
        
        for n in arr:
            while st and st[-1]<=n:
                curr=st.pop()
                if st: res+=curr*min(st[-1],n)
            st.append(n)
            
        while len(st)>2:
            res+= st.pop()*st[-1]
        return res
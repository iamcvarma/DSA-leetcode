class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for c in s:
            if st and st[-1][0]==c:
                st.append((c,st[-1][1]+1))
                if st[-1][1]==k:
                    for _ in range(k):
                        st.pop()
            else:
                st.append((c,1))
        return "".join([c[0] for c in st])
            
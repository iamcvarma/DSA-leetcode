class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        s = list(s)
        for i,c in enumerate(s):
            if c=='(':
                st.append(i)
            elif c==')':
                if st:st.pop()
                else:s[i]=""
        for i in st:
            s[i]=""
        return "".join(s)                    
            
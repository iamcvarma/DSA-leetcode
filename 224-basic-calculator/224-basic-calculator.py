class Solution:
    def calculate(self, s: str) -> int:
        def calc(curr,num,sign):
            return (curr+num) if sign=='+' else num-curr
        s = s+'+0'
        curr=0
        st=[(0,'+')]
        for c in s:
            if c==' ':continue
            elif c=='(':
                st.append((0,"+"))
            elif c==')':
                curr = calc(curr,*st.pop())
            elif c in ("+","-"):
                st.append((calc(curr,*st.pop()),c))
                curr=0
            else:
                curr = curr*10+int(c)
        return st.pop()[0]
                    
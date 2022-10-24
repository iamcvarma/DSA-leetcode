class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        for _dir in path.split('/'):
            if st and _dir=="..":
                st.pop()
            elif _dir != "" and _dir != "." and _dir!="..":
                st.append(_dir)
        return '/'+'/'.join(st)
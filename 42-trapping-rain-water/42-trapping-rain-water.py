class Solution:
    def trap(self, arr: List[int]) -> int:
        res = 0
        st=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]<=arr[i]:
                curr = st.pop()
                if st:
                    j = st[-1]
                    res+=(min(arr[j],arr[i])-arr[curr])*(i-j-1)
            st.append(i)
        return res
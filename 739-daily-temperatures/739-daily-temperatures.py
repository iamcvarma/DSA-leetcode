class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res=[0]*n
        st=[]
        for i in range(n):
            while st and arr[st[-1]]<arr[i]:
                temp = st.pop()
                res[temp] = i-temp
            st.append(i)
        return res
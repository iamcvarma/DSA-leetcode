class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0]*n
        right = [n-1]*n
        st=[]
        for i in range(n):
            while st and arr[st[-1]]>=arr[i]:
                right[st.pop()]=i-1
                
            if st: left[i] = st[-1]+1
            st.append(i)
        return sum((i-left[i]+1)*(right[i]-i+1)*arr[i] for i in range(n))%(10**9+7)
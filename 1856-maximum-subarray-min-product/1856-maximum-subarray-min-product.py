class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 1000000007
        pre = [0]*(n+1)
        for i,v in enumerate(nums):
            pre[i+1]=pre[i]+v
        
        left,right = [0]*n,[n-1]*n
        st=[]
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if st:left[i] = st[-1]+1
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if st:right[i] = st[-1]-1
            st.append(i)
        ma=0
        for i in range(n):
            s = pre[right[i]+1]-pre[left[i]]
            ma = max(ma,s*nums[i])
        return ma%mod
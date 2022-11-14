class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n = len(nums)
        res = [-1]*n
        for i in range(n):
            while st and nums[st[-1]]<nums[i]:
                x = st.pop()
                res[x] = nums[i]
            st.append(i)
        
        for i in range(n):
            while st and nums[st[-1]]<nums[i]:
                x = st.pop()
                res[x] = nums[i]
            st.append(i)
        return res
        
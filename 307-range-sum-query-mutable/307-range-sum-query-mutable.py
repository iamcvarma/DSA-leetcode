class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            self.add(i,nums[i-1])
        return
    
    def add(self,i,val)->None:
        while i<len(self.arr):
            self.arr[i]+=val
            i+=(i&-i)
        return None
    
    def calcSum(self,index)->int:
        res=0
        while index:
            res+=self.arr[index]
            index-=(index& -index)
        return res
    
    def update(self, index: int, val: int) -> None:
        curr_sum = self.sumRange(index,index)
        diff = val-curr_sum
        self.add(index+1,diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.calcSum(right+1)-self.calcSum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
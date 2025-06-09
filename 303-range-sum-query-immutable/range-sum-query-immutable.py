class NumArray:

    def __init__(self, nums: List[int]):
        #build array of nums
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        #add ints for left and right+1
        x = sum(self.nums[left:right+1])
        return x

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
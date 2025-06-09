class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            output ^= num
        return output
        #for each number in the array
            #check each number in list sequentially 
        #return single number
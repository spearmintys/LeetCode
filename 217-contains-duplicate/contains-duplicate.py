class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #setup arrays
        singles = set()
        #for each value in array    
        for num in nums:
            #capture value then compare
            if num in singles:
                return True
            else:
               #true false return
                singles.add(num)
        return False
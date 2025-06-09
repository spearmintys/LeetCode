class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #output = 0
        #for num in nums:
        #    output ^= num
        #return output
        #for each number in the array
            #check each number in list sequentially 
        #return single number


        #brute force
        counts = {}
        #how many time that num appears
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
       #what number has 1 count
        for num in counts:
            if counts[num] == 1:
                return num

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        test = set()
        for i in range(len(nums)):
            if nums[i] in test:
                return True
            test.add(nums[i])
            if len(test) > k:
                test.remove(nums[i - k])
        return False

        #brute force
        #double nested for loop
        #for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
            #loop though to check num 
        #        if nums[i] == nums[j] and abs(i - j) <= k:
                #nums[i] == nums[j]
                    #then loop to check ijk
                    #abs(i - j) <= k
        #            return True
        #return False


        #optimized
        #test = {}
        #for i in range(len(nums)):
        #    if (nums[i] in test) and (abs(i - test[nums[i]] <= k)):
        #        return True
        #    else:
        #        test[nums[i]] = i
        #return False
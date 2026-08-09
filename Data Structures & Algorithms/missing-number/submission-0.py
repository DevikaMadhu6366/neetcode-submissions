class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i]) 
            # we want all nos from range 0-n bt we have nums[i] already
            #subtract both to get what wedont have and add it to 0 and storein res
        return res

        #nums = [3,1,0] len(nums = 3) i in range[0,1,2,3]
        # first sub then add

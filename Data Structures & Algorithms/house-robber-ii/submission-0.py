class Solution:
    def rob(self, nums: List[int]) -> int:
         return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob2,rob1=0,0
        #rob1,rob2,n,n+1...
        for num in nums:
            temp = max(rob2,num+rob1)
            rob1 = rob2
            rob2 = temp
        return rob2 # coz rob 2 will be last value which is max upto last eleamnt




class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        res = nums[l]
        while l <=r:
            mid = (l + r)//2
            res = min(res,nums[mid])
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return res
            


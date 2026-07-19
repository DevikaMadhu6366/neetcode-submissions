class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 #left pointer
        r = len(nums)-1 #right pointer

        while l<=r:
            m = (l+r)//2 #mid
            if nums[m]> target:
                r = m-1
            elif nums[m] < target:
                l=m+1
            else:
                return m
            
        return -1

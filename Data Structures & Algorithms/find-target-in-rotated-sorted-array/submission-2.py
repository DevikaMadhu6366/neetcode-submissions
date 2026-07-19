class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l<=r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid


            if nums[l] <= nums[mid]: # left is sorted part
                if target > nums[mid] or target < nums[l]:#to check if it belongs to left part or notie if excluded
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:#excluded from right part
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
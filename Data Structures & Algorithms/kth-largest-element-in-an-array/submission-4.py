class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k   
        def partition(l,r):
            pivot = nums[r]
            i = l
            for j in range(l,r):
                if nums[j] <= pivot:
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
            nums[i],nums[r] = nums[r], nums[i]
            return i
                

        l,r = 0,len(nums)-1
        p = len(nums)

        while p != k :
            p = partition(l,r)
            if p < k:
                l = p + 1
            else:
                r = p - 1
        return nums[k]

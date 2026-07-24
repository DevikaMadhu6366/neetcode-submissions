class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = [] # for each element  2 choices include it or exclude it so results in a decision tree

        def dfs(i):  # i is index of value we are passing
            if i >= len(nums):
                res.append(subset.copy())
                return

            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #decision to exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
        



             
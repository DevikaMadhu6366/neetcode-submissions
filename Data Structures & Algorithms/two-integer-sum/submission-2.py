class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # to store index and Value of each number

        for i,n in enumerate(nums):
            complement = target - n

            if complement in hashMap:
                return[hashMap[complement],i]  # expected return type is  alist
            hashMap[n] = i
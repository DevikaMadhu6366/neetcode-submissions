class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        count = {}
        for num in nums :
            count[num] = 1 + count.get(num,0) # take the count of each numberadd 1 to existing count 

        freq = [[] for i in range(len(nums) + 1)]# we need one outer list containing many inner lists[[] [] []...]
        for n,c in count.items():
            freq[c].append(n)#add value of num to corresponding freq list

        res = []
        for i in range(len(freq) - 1,0,-1):# traverse backward
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        
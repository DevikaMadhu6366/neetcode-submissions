class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        count = {}
        for num in nums :
            count[num] = 1 + count.get(num,0) # take the count of each numberadd 1 to existing count 

        freq = [[] for i in range(len(nums) + 1)]# we need one outer list containing many inner lists[[] [] []...]
        for n,c in count.items():  #ie create buckets or list freq with its index as freq
            freq[c].append(n)#add value of num to corresponding freq list

        res = []
        for i in range(len(freq) - 1,0,-1):# traverse backward
            for n in freq[i]:
               res.append(n) # add most freq elemnts to res from highest freq
               if len(res) == k:  #k no of most freq elements = length of res then return 
                   return res  # ie when no of elemnts in res equal to k no of elemnts tthen return
        
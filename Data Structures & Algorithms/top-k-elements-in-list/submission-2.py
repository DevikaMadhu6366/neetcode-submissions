class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         count = {}
         for num in nums:
            count[num] = 1 + count.get(num,0)
         
         freq = [[] for i in range(len(nums) + 1)]
         for n,c in count.items():#returns all key value pairs
            freq[c].append(n)
         
         res = []
         for i in range(len(freq) - 1,0,-1):
            for n in freq[i]: # n is the highest freq element
               res.append(n) # add it to res
               if len(res)== k: # return k no of highest freq elements
                  return res
               

                    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         res = defaultdict(list) #resultant list of angrams to be returned
        
         for s in strs:# loop through each word in strs
               count = [0] * 26 
               for c in s: # loop through each char in word
                   count[ord(c) - ord('a')] += 1
               res[tuple(count)].append(s)
         return list(res.values())
      

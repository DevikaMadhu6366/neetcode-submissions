class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if  (1 << i) & n: # create a mask with only i th bit set 
                res += 1      # check if this bit is set in n
        return res
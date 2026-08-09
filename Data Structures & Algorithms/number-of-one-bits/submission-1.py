class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1 if n & 1 else 0
            n >>= 1
        return res

#checking only least significant digit at each step
#res inc only if LSB is 1 so & 1 will be true n = n >> 1
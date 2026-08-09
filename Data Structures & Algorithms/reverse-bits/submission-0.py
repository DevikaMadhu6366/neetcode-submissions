class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # exctracting digits at each position and with 1
            res += (bit << (31 - i))
        return res
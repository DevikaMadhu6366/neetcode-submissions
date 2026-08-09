class Solution:
    def countBits(self, n: int) -> List[int]:
        dp =[0] * (n +  1) # To store no of set bits in i,no of 1 in bin rep of i
        offset = 1 # Tracks most recent power of 2

        for i in range(1,n+ 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset] # remainder + 1 for no which are not pow(2)
        return dp

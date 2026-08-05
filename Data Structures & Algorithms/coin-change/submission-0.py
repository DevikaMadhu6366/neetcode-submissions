class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #"I have a slot for every amount, and initially I don't know the answer, so I'll put a large value there."
        dp = [amount + 1]* (amount + 1) 
         #dp = [6, 6, 6, 6, 6, 6]
        dp[0] = 0
        for a in range(amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a] ,1 + dp[a - c])
                
        return dp[amount] if dp[amount] != amount + 1 else -1
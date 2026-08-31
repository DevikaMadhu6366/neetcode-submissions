class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i):
            # Base cases
            if i <= 2:
                return i

            # Already calculated
            if i in memo:
                return memo[i]

            # Calculate and store
            memo[i] = dfs(i - 1) + dfs(i - 2)

            return memo[i]

        return dfs(n)
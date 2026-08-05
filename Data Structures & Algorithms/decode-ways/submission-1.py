class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s) : 1}

        def dfs(i): #if dp[2]=1 then dfs(2) gives 1 dont recompute
            if i in dp: # if already calculated no of ways for value at i return 
                return dp[i]# no need of recomputing dp value again using dfs()
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res #Store the value so that no need to recalculate again
            return res

        return dfs(0)
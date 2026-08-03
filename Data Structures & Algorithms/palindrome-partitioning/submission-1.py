class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur =[]
        res=[]

        def isPali(s,l,r):
            while l < r:
                if s[l] != s[r]:
                  return False
                l,r = l+1,r-1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(cur.copy())
                return 
            for j in range(i,len(s)):
                if isPali(s,i,j):
                    cur.append(s[i:j+1])
                    dfs(j + 1)
                    cur.pop()#backtracking remove last element

        dfs(0)
        return res

    


           
            



            
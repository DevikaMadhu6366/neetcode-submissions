class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        cur=[] #string dod not support pop and append fns we use string instead
        if not digits:
            return res
        digitToChar ={ #Tells what choice we have for each digit
            "2": "abc",
            "3": "def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz",

        }
        def dfs(i): # i : which digit currently processing 0th index-2,1stindex-3
            if i == len(digits):# have I processed all digits 
                res.append("".join(cur))
                return 
             
            letters = digitToChar[digits[i]] # digits[0]=2 and digits[1]=3
            for char in letters:
                cur.append(char)
                dfs(i+1)
                cur.pop()

        dfs(0)
        return res
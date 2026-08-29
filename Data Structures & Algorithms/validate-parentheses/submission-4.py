class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[] #create a stack
        closeToOpen= {")" :"(","]" :"[","}" :"{"} # dictionary mapping to check for each close bracket if open bracket is matching
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # top of stack is value coresponding to key in c
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack :
           return True
        else:
           return False
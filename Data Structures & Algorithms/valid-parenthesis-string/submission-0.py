class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star =[]
        for i ,ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:#right para occurs
                if not left and not star:#Both are empty
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        while left and star:#for remaining char
            if left.pop() > star.pop():#index of left > index of star
                return False
        return not left


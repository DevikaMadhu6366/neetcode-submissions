class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin,leftMax =0,0
        
        for c in s:
            if c == "(":
                leftMin,leftMax = leftMin + 1,leftMax + 1
            elif c == ")":
                leftMin,leftMax = leftMin - 1,leftMax - 1
            else:
                leftMin,leftMax = leftMin - 1,leftMax + 1
            if leftMax < 0: # it dec only when ) occurs sotoo many ) when neg
                return False
            if leftMin < 0: # still potentially valid coz ift dec may be due to *
                leftMin =0
        return leftMin == 0

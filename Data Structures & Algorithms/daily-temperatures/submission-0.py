class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack =[] # pair[temp,index]

        for i,t in enumerate(temperatures): #get value and index together
            while stack and t > stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = (i - stackInd) # diff in index of current temp(greater) and popped temp 
            stack.append([t,i])
        return res

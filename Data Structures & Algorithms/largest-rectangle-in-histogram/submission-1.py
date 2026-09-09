class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]> h:
            #stack top elem h ids larger than height at next index 
                index,height = stack.pop()#pop:coz that ele cannot extend to right
                maxArea = max(maxArea,height *(i-index)) 
                start = index
            stack.append((start,h))#push: we can extend from left ie poped ele index and python list accept only one arguement so push as tuple of 2 elements

        for i,h in stack:
            maxArea = max(maxArea,h * (len(heights)-i))
        return maxArea









            
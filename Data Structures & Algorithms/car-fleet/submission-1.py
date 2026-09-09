class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Because a car behind another car can potentially catch the car in front.

#So we need to know what happens to the car ahead first.

        pair = [[p,s] for p,s in zip(position,speed)]
        pair.sort(reverse = True)
        stack =[]
        for p,s in pair:
            stack.append((target-p)/s)
        
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                #cuttenttime <= fronttime
                stack.pop()
        return len(stack)
                
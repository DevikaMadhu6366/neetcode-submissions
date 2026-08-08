class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        res = []

        for i in range(len(intervals)):# end of curr int < strt of next interval

            if newInterval[1] < intervals[i][0]: #intervals before new not overlap
                  res.append(newInterval)
                  return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval =[
                    min(newInterval[0],intervals[i][0]),
                    max(newInterval[1],intervals[i][1]),
                ]
        res.append(newInterval) #if intervals over then append new at end 
        return res


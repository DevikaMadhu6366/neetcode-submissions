class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap =[]
        res ={}
        i =0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]#get all the intervals
                heapq.heappush(minHeap,(r - l + 1,r))
# we also need right index to check if r >= q since already checked left  
                i+= 1
            while minHeap and minHeap[0][1] < q:#heap =[size,end]
               heapq.heappop(minHeap) #pop all invalidintervals getsmallestvalid 
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
 

                
            

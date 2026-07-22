class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) #heapq ia a python module library that rearanges stones

        while len(stones) > 1:# keep repeating until there are two elements left 
            first = heapq.heappop(stones) # largest element
            second = heapq.heappop(stones) # second largest element
            if second > first: # it means if first > second bt since they are negative values sign reversed
                diff = first - second # to avoid negative value larger - smaller
                heapq.heappush(stones,diff)

        stones.append(0)
        return abs(stones[0])
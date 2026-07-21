class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k = nums,k # create minheap  and initialise k 
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) >self.k:
            heapq.heappop(self.minHeap) # remove smallest element heap root until it contains k elemnts
        return self.minHeap[0] #  return kth largest which is heaps smallest element
        

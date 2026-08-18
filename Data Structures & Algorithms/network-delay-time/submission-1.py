class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times: #create adictioanry and add adj vertices and their w 
            edges[u].append((v,w))

        minHeap = [(0,k)]#time nad node
        visit = set()#to avoid reprocessing node
        t = 0
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)# it will pop node with min w since it is min heap
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1) #weight1 is time it takes to reach node1

            for n2,w2 in edges[n1]:
                if n2 not in visit:#push all the unvisited neighbours to heap
                    heapq.heappush(minHeap,(w1 + w2,n2))

        return t if len(visit) == n else - 1 #after minHeap is empty return timeie after all nodes are visited
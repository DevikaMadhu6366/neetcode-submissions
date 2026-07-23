class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

       # dist = lambda x : x[0] ** 2 + x[1] ** 2
        def euclidean(points):
            x, y = points
            return x**2 + y**2

        def partition(l,r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l,r):
                if euclidean(points[j]) <= pivotDist:  
                    points[i],points[j] = points[j] ,points[i]# if jth element dist is less than pivot dist then bring jth element to ith position 
                    i += 1
            points[i] ,points[r] = points[r] , points[i] #if jth element dist larger than pivot dist then bring pivot to ith position
            return i # return the position of pivot


        l,r = 0,len(points)-1
        pivot = len(points)

        while pivot != k:
            pivot = partition(l,r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]
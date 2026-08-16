class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Build an adjacency list of prereq or build grapg crs pts to prereq
        preq = {i :[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preq[crs].append(pre)
        
        output = []
        visit,cycle = set(),set()

        def dfs(crs):
            if crs in cycle:#crs is present in path of cycle
                return False
            if crs in visit:#crs has already been added to output
                return True#This may occur when alraedy added value becom prereq 
            
            cycle.add(crs)#crs is unvisited
            for pre in preq[crs]:
                if dfs(pre) == False:#cycle detected
                    return False
            cycle.remove(crs)#if all Dfs succes and no cycle,remv crs from cycle 
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
            
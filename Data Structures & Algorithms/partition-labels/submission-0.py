class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i,c in enumerate(s): #update at each index of c
            lastIndex[c] = i

        res = []
        size,end = 0,0
        for i,c in enumerate(s):
            size += 1
            end = max(end ,lastIndex[c])

            if i == end :
                res.append(size)
                size =0
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output =[]
        q=deque()
        l=0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]: # input elemeent ids greater than top element in queueu
                q.pop()
            q.append(r) #push the index to q
        

            if l > q[0]:
              q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
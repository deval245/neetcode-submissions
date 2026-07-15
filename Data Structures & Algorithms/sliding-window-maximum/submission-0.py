from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            # Remove indices of elements not in the current window
            if q and q[0] == i - k:
                q.popleft()

            # Remove from back if current element is greater
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            # Add current index
            q.append(i)

            # Add to result when window is full
            if i >= k - 1:
                res.append(nums[q[0]])  # q[0] is index of max

        return res

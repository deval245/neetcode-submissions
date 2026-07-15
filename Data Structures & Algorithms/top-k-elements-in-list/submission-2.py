from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minheap = []

        for i,num in freq.items():
            heapq.heappush(minheap,(num,i))
            if len(minheap)>k:
                heapq.heappop(minheap)

        result =[]
        while minheap:
            result.append(heapq.heappop(minheap)[1])
        return result    
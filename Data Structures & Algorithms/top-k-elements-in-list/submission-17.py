
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        min_heap =[]

        for i,num in freq.items():
            heapq.heappush(min_heap,(num,i))

            if len(min_heap) >k:
                heapq.heappop(min_heap)   

        result =[]
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result    
                
        
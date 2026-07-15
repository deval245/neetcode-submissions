class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freq_counter = Counter(nums)
        max_heap = []

        for i ,num in freq_counter.items():
            heapq.heappush(max_heap,(-num,i))

        result =[] 
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1]) 
        return result      
        
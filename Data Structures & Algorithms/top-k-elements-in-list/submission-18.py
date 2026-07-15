from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        print(freq)
        sorted_item =sorted(freq.items(), key = lambda x:x[1] ,reverse =True)
        print(sorted_item)
        return [item[0]for item in sorted_item[:k]]
        


        
from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = Counter(nums)
        print(freq)

        for i in freq.values():
            if i >= 2:
                return True
          
        return False    

        
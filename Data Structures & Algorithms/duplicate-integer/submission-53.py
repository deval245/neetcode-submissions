class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = dict()


        for num in nums:

            if num in freq:

                return True
            freq[num] =num 
        return False     
        
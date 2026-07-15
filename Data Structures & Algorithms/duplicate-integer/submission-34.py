class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return False
        freq = set()   

        for num in nums:
            if num in freq:
                return True
            freq.add(num)    
        return False         

        
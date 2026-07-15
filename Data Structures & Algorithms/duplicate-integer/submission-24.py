class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #[1,2,3,4,4]

        freq = set()
        for num in nums:
            if num in freq:
                return True
            freq.add(num) 
        return False       
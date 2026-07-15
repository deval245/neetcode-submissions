class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c_map = {}  

        for i, num in enumerate(nums):
            complement = target - num  
            
            if complement in c_map:
                return [c_map[complement], i]  
            
            c_map[num] = i   
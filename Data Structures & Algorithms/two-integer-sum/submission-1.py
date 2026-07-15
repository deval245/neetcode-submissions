class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums)<= 1:
            return False
        if target is None :
            return False    

        n ={}
        for key,value in enumerate(nums):
            comp_n = target -value
            if comp_n in n:
                return [n[comp_n],key]
            n[value]=key
        return []    

            
                

    
        
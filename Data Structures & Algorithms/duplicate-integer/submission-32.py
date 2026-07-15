class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums)<=1:
            return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)) :
                if nums[i] == nums[j]:
                    return True
        return False            


        
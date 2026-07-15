class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left =0
        


        for right in range(1,len(nums)):

            if nums[right]== nums[left]:
                return True
            left+=1
        return False
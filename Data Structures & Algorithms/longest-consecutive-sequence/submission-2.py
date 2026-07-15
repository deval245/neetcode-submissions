class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        longest =count =0

        for i,num in enumerate(nums):
            count =count+1 if i> 0 and nums[i]==nums[i-1]+1 else 1
            longest = max(longest,count)
        return longest    
        
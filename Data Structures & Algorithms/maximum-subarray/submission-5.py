class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total_sum = nums[0]
        current_sum =0

        for num in nums:
            current_sum = max(current_sum,0)
            current_sum += num
            total_sum = max(total_sum,current_sum)
        return total_sum    
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #input = [2,20,4,10,3,4,5]

        if len(nums) < 1:
            return 0

        nums = sorted(list(set(nums))) # [2,3,4,5,10,20]

        n = len(nums) # 5
        max_len = 1
        current_len = 1

        for i in range(1,n):
            if (nums[i] - nums[i-1]) == 1:
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
        return max_len
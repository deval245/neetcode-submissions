class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0

        length =0
        nums.sort()
        max_len = float('-inf')

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                length+=1
            elif nums[i] - nums[i-1]>1:
                length=0
            max_len= max(max_len,length+1) 
        return max_len if max_len != float('-inf')  else 1

        
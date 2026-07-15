class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total =0

        curr_max=curr_min =0
        gl_max=gl_min = nums[0]

        for num in nums:

            total+=num
            curr_max = max(curr_max+num,num)
            gl_max= max(gl_max,curr_max)

            curr_min = min(num,curr_min+num)
            gl_min = min(gl_min,curr_min)

        if gl_max< 0:
                return gl_max

        return max(gl_max, total-gl_min)         

        
        
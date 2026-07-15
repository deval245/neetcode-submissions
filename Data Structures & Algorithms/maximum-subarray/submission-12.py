class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """" lets do some dry run 
        input array lets say.: [2,-3,4,-2,2,1,-1,4]
        
        if len(nums)==0: return 0 here len is not null so not fall in this edgecase

        max_sum =nums[0] its set to 0th index which is 2 
        curr_sum =0

        iteration start 
        curr_sum = max(curr_sum,0) here we checking that curre_sum should not be negative or lessthe
        zeor
        1st iteration 2+0 =2. currentsum+=num = 2 currentsum= 2
        2nd iteration 2+-3  currentsum -1 so its fall under condition of curr_sum = max(curr_sum,0)
        so thats reason now again curr_sum become 0
        3rd iteration 4+currentsum=0  so now currentsum =4
        4th iteration 4+-2   so current sum =2
        5th iteration 2+2 so current sum =4
        6th iteration 4+1  current sum =5
        7th iteration 5+-1 = 4 current sum =4
        last iteration 4+4 = current_sum =8
        then  max_sum = max(max_sum,curr_sum). max_sum = (2,8)
        return max_sum


        """

        if len(nums)==0: return 0

        max_sum =nums[0]
        curr_sum =nums[0]


        for i in range(1,len(nums)):
            curr_sum = max(nums[i],curr_sum+nums[i])

            max_sum = max(max_sum,curr_sum)
        return max_sum    
        
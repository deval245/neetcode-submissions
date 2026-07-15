class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq ={} # {3:0}

        for i ,num in enumerate(nums):# (0:3,1:4,2:5,3:6)
            comp = target-num #first iter 7-3  comp =4 ,3,

            if comp in freq:
                return [freq[comp],i] #[0,1]
            freq[num]= i   

        return []     

        
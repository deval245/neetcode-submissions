class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        output =[]
        n = len(nums)
        ap = n//3
        freq = dict()


        for num in nums:
            freq[num] = freq.get(num,0)+1
        for key,value in freq.items():
            if value >ap:
                output.append(key)  
        return output          
          

          



        
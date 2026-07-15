class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = dict()


        for num in nums:

            seen[num]= seen.get(num,0)+1

        for key,value in seen.items():

            if value >1:

                return key

               




        

        
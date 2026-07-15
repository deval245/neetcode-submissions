class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        Maj_element =0
        freq = {}

        for num in nums:
            freq[num] =freq.get(num,0)+1

        sorted_num = sorted(freq.items(),key = lambda item:item[1],reverse =True)   

        return sorted_num[0][0]








        
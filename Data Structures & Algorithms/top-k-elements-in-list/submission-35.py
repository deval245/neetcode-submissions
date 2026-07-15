class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = dict()

        for num in nums:

            freq[num] = freq.get(num,0)+1

        sorted_num = sorted(freq.items(),key = lambda item:item[1],reverse = True) 

        return [item[0]for item in sorted_num[:k]]
        
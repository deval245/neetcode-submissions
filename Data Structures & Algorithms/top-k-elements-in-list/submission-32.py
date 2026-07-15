from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        """

        dry run here  

        nums = [1,2,2,3,4,4,5,5]

        freq = {1:1,2:2,3:3,4:2,5:2}
        sorted_nums = {5:2,4:2,3:3,2:2,1:1}
        

        """

        sorted_nums = sorted(freq.items(),key = lambda x:x[1],reverse=True)
        return [num for num,count in sorted_nums[:k]]
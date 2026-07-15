class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        freq = {}

        for i ,num in enumerate(numbers):
            comp = target-num
            if comp in freq:
                return [freq[comp]+1,i+1]
            freq[num] = i
        return []
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        freq = set(nums)

        lo_seq =0

        for n in nums:
            if (n-1) not in freq:
                length =0
                while(n+length) in freq:
                    length +=1
                lo_seq = max(length,lo_seq)   
        return lo_seq         


        
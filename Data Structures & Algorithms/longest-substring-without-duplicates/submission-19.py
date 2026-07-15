class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freq = set()

        max_len =0

        L =0

        for R in range(len(s)):
            while s[R] in freq:
                freq.remove(s[L])
                L+=1
            freq.add(s[R])   
            max_len = max(max_len,R-L+1) 
        return max_len    
        
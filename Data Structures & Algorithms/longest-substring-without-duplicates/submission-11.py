class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0

        freq = set()
        l =0
        max_len = 0

        for r in range (len(s)):
            while s[r]  in freq:
                freq.remove(s[l])
                l+=1
            freq.add(s[r])
            max_len = max(max_len,r-l+1)    

        return max_len    
        
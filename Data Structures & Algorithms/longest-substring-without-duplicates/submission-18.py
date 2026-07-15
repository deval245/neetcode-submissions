class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0

        max_len =0

        l =0
        freq = set()

        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l+=1
            freq.add(s[r]) 

            window = r-l+1
            max_len = max(max_len,window)   

        return max_len    
        
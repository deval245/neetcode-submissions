class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s : return 0

        max_len =0
        l =0
        char_map = set()

        for r in range(len(s)):

            while s[r] in char_map:
                char_map.remove(s[l]) 
                l+=1
            char_map.add(s[r])    
            max_len = max(max_len, r-l+1)
        return max_len         
        
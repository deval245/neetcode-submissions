class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        char_map = set()
        l =0
        res=0

        for r in range(len(s)):
            while s[r]in char_map:
                char_map.remove(s[l])
                l+=1
            char_map.add(s[r])
            res = max(res,r-l+1)
        return res        
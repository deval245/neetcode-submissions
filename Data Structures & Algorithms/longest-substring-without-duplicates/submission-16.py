class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0


        max_len =0

        for i in range(len(s)):
            seen = set()

            for j in range(i,len(s)):

                if s[j] in seen:
                    break
                seen.add(s[j]) 
                window = j-i+1

                max_len = max(max_len,window)   
        return max_len        




        
        
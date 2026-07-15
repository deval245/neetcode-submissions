class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        left =0
        mx =0

        for right  in range(len(s)):

            char =s[right]
            while char  in seen:
                seen.remove(s[left])
                left+=1
            seen.add(char)    
            mx = max(mx,right-left+1)
        return mx    

                    



        
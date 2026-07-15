class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = set()
        count =0
        l=0
        string =""
        result =0

        for r in range(len(s)):
            while s[r] in char_map:
                char_map.remove(s[l])
                l+=1
            char_map.add(s[r])
           
            if r-l+1 > count:
                count = r-l+1
                result = s[l:r+1]
        
        print(result)    
        return count      


        
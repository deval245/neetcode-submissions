
from collections import Counter

class Solution:
    def minWindow(self,s,t):
        
        """ minimum window substring hard question leetcode 76 sliding window, hasmap twopointer three patterns are involved in it
         Input: s = "ADOBECODEBANC", t = "ABC"
         Output: "BANC"
         Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
         
         
         Input: s = "a", t = "aa"
         Output: ""
         Explanation: Both 'a's from t must be included in the window.
         Since the largest window of s only has one 'a', return empty string.

        
        """
        if not t or not s: # if there is no value in both string
            return ""
            
        t_count = Counter(t)    ## Ex: {'A':1, 'B':1, 'C':1}
        window ={} # char_in current_window
        have,need =0,len(t_count) # have many char matched.
        res = [-1,-1] # final window start & end.
        res_len = float('inf') # len of best window
        l =0 # left pointer
        
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char,0)+1
            print(f"Added: {char}, window: {window}")
            
            
            
            if char in t_count and window[char]== t_count[char]:
                have+=1
            while have ==need:
                if (r-l+1) < res_len:
                    res =[l,r]
                    res_len = r-l+1
                    print(res,res_len,have,need)
                window[s[l]]  -=1
                if s[l] in t_count  and window[s[l]]< t_count[s[l]]:
                    have-=1
                l +=1
        l,r =res
        return s[l:r+1] if res_len != float('inf')else ""
        
        
        


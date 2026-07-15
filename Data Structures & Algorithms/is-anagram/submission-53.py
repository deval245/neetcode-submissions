class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t)!= len(s):
            return False

        freq = {}    

        for char in s:
            freq[char] = freq.get(char,0)+1
        for char in t:
            freq[char] = freq.get(char,0)-1

        for value in freq.values():
            if value !=0:
                return False
        return True
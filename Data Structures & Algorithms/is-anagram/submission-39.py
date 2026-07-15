class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq ={}
        if len(s)!= len(t):
            return False


        for char in s:
            freq[char] = freq.get(char,0)+1
    
        for char in t:
            freq[char] = freq.get(char,0)-1

        return all(value ==0 for value in freq.values())    



        
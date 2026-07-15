class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if len(s)!= len(t):
            return False

        freq = {}

        for x,y in zip(s,t) :

            freq[x] = freq.get(x,0)+1
            freq[y] = freq.get(y,0)-1
        return all(value==0 for value in freq.values())    


        
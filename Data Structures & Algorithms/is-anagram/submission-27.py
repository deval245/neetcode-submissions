class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        # # freq ={}
        # if len(s) != len(t): return False

        # # for x,y in zip(s,t):
        # #     freq[x]=freq.get(x,0)+1
        # #     freq[y]=freq.get(y,0)-1

        # # return all(c==0 for c in freq.values())    
        # freq =[0]*26

        # for i in range(len(s)):
        #     freq[ord(s[i])-ord('a')]+=1
        #     freq[ord(t[i])- ord('a')]-=1
        # return all(c==0 for c in freq)    
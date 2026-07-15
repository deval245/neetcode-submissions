class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False

        if len(s) != len(t):
                return False

        reversed_t =t[::-1]
        if sorted(s) == sorted(reversed_t):
            return True
        return False    

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count ={}

        for char in s:
            char_count[char]= char_count.get(char,0)+1
        for char in t:
            if char in char_count:
                char_count[char]-=1
                if char_count[char]< 0:
                    return False
            else:
                return False    
        return all(count == 0 for count in char_count.values())                
        
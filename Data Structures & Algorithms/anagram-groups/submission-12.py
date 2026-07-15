class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = defaultdict(list)
        for word in strs:
            freq =[0]* 26
            for char in word:
                freq[ord(char)- ord('a')]+=1
            anagram[tuple(freq)].append(word)  
        return list(anagram.values())      
        
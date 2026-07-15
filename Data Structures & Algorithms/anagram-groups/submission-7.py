from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for ch in word:
                freq[ord(ch)- ord('a')]+=1
            key = tuple(freq)
            anagram[key].append(word)
        return list(anagram.values())        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         anagrams = defaultdict(list)  # Initialize dictionary to group anagrams

         for word in strs:  
            count = [0] * 26  
            
        
            for char in word:
                count[ord(char) - ord('a')] += 1

       
            signature = tuple(count)
            anagrams[signature].append(word)  # Append the word to its group

       
         return list(anagrams.values())
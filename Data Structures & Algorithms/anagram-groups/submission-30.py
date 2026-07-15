class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        group = dict()

        for ch in strs:

            key = ''.join(sorted(ch))

            if key not in group:

                group[key] = []
            group[key].append(ch) 
        return list(group.values())       
        
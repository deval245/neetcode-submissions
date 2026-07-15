class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <1 : return []

        group = {}

        for ch in strs:
            key = ''.join(sorted(ch))
            if key not in group:
               group[key]  = [] 
            group[key].append(ch)   

        return list(group.values())     

            




            
        
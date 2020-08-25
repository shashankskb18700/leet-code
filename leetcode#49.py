class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        ht={ }
        for string in strs:
            
            ss=''.join(sorted(string))
            if ss in ht:
                ht[ss].append(string)
            else:
                ht[ss]=[string]
        return ht.values()

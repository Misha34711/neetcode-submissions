class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for j in strs:
            
            a="".join(sorted(j))
            if a in d:
                d[a].append(j)
            else:
                d[a]=[j,]            
        return list(d.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         l=[]
         d={}
         for i in strs:
            j="".join(sorted(i))
            if j in d:
                d[j].append(i)
            else:
                d[j]=[i]
         for i,j in d.items():
            l.append(j)
         return l


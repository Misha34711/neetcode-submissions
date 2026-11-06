class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         l=[]
         d={}
         for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord("a")]+=1
            if tuple(count) not in d:
                d[tuple(count)]=[i]
            else:
                d[tuple(count)].append(i)
         for x,y in d.items():
               l.append(y)
         return l
                


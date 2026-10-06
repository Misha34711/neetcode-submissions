class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for i in s:
            d1[i]=d1.get(i,0)+1
        for j in t:
            d2[j]=d2.get(j,0)+1
        for i in s:
            if d1[i]!=d2.get(i,0):
                return False
        return True        
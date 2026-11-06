class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1={}
        for i in s:
            d1[i]=d1.get(i,0)+1
        for j in t:
            d1[j]=d1.get(j,0)-1
        for i in d1:
            if d1[i]!=0:
                return False
        return True
        
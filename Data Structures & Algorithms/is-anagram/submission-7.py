class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1=[0]*26
        for i in s:
            d1[ord(i)-ord('a')]+=1
        for j in t:
            d1[ord(j)-ord('a')]-=1
        for i in d1:
            if i!=0:
                return False
        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=0
        d=""
        for i in s:
            if i.isalnum():
                d+=i.lower()
        j=len(d)-1
        while(k<j):
            if(d[k]!=d[j]):
                return False
            k+=1
            j-=1
        return True
        
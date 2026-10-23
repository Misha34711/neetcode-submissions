class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        d="".join(l)
        if d==d[::-1]:
            return True
        else:
            return False
        
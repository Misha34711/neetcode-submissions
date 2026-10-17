class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        p=[]
        s=[1]*n
        pre=1
        suf=1
        for i in range(n):
            p.append(pre)
            pre*=nums[i]
            s[n-1-i]=suf
            suf*=nums[n-1-i]
        for i in range(n):
            l.append(p[i]*s[i])
        return l

            

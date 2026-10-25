class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        for j in range(len(nums)):
            s={}
            for i in range(j+1,len(nums)):
                if -nums[j]-nums[i] in s:
                    a=sorted([nums[j],nums[i],-nums[j]-nums[i]])
                    if a not in l:
                        l.append(a)
                s[nums[i]]=i
        return l

        
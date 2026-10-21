class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c=1
        s=set()
        if len(nums)==0:
            return 0
        for i in nums:
            s.add(i)
        for i in s:
            t=1
            if i-1 in s:
                continue
            else:
                tp=i
                while tp+1 in s:
                    t+=1
                    tp+=1
                c=max(t,c)
        return c

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        b=[[] for i in range(len(nums)+1)]
        for x in d:
            b[d[x]].append(x)
        l1=[]
        i=0
        for x in range(len(b)-1,-1,-1):
            for j in b[x]:
                l1.append(j)
            if len(l1)>=k:
                return l1
        return l1
        



    
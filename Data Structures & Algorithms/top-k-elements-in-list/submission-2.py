class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        l=sorted(list(d.items()),key=lambda x:x[1],reverse=True)
        l1=[]
        for i in range(k):
            l1.append(l[i][0])
        return l1

        
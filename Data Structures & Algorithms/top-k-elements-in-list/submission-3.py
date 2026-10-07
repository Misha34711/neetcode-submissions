class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        l=[[] for i in range(len(nums)+1)]
        for i,j in d.items():
            l[j].append(i)
        count=0
        ans=[]
        for i in range(len(l)-1,-1,-1):
            for x in l[i]:
                if(count!=k):
                    ans.append(x)
                    count+=1
        return ans


        
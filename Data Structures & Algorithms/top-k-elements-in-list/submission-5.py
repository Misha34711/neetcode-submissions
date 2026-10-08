class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        l=sorted(d,key=lambda x:d[x])
        c=0
        a=[]
        for i in range(len(l)-1,-1,-1):
            if(c!=k):
                a.append(l[i])
                c+=1
        return a
            
        



        
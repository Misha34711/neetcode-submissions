class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        l=sorted(d.items(),key=lambda p:p[1])
        c=0
        a=[]
        for i in range(len(l)-1,-1,-1):
            if(c!=k):
                a.append(l[i][0])
                c+=1
        return a
            
        



        
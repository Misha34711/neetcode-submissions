class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"$"+i
        return s



    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while (i<len(s)):
            j=i+1
            while(s[j]!="$"):
                j+=1
            n=int(s[i:j])
            s1=""
            for x in range(j+1,j+1+n):
                s1+=s[x]
            l.append(s1)
            i+=n+1+len(s[i:j])
        return l
            
                
                

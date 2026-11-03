class Solution:

    def encode(self, strs: List[str]) -> str:
        l=""
        for i in strs:
            
                l=l+(str(len(i))+"#"+i)
        
        return l


    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
    
        while(i<len(s)):
            j=i
            while(s[j]!='#'):
                j+=1
            length=int(s[i:j])
            l.append(s[j+1:j+1+length])
            i=length+j+1
            
        return l




              

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r=0
        l=0
        d={}
        a={}
        for i in s1:
            if i not in d:
                d[i]=s1.count(i)
        while(r<len(s2)):
            if(s2[r] in s1 and s2[r-1] not in s1 and r!=0):
                l=r
                if(s2[r] not in a):
                    a[s2[r]]=1
                else:
                    a[s2[r]]+=1
                r+=1
            elif(s2[r] in s1):
                if(s2[r] not in a):
                    a[s2[r]]=1
                else:
                    a[s2[r]]+=1
                if(a[s2[r]]>d[s2[r]]):
                    while(a[s2[r]]>d[s2[r]]):
                        if(s2[l]==s2[r]):
                            a[s2[r]]-=1
                        l+=1

            

                else:
                    if(d==a and len(s1)==(r-l+1)):
                        return True
                    
            
                r+=1
            else:
                a={}
                r+=1
        
        return False
            
                



        
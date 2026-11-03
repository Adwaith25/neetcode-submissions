class Solution:
    def trap(self, height: List[int]) -> int:
        l=[]
        r=[]
        l_max=0
        for i in range(len(height)):
            if(i==0):
                l.append(0)
                continue
            l_max=max(l_max,height[i-1])
            l.append(l_max)
           
        r_max=0
        for i in range(len(height)-1,-1,-1):
            if(i==len(height)-1):
                r.append(0)
                continue
            r_max=max(r_max,height[i+1])    
            r.append(r_max)
        r=r[::-1]
        
        s=0
        for i in range(len(height)):
            a=min(l[i],r[i])-height[i]
            if a>0:
                s+=a
        return s
        
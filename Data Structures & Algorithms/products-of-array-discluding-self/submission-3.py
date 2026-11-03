class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        a=1
        for i in range(len(nums)):
            l.append(a)
            a=a*nums[i]
        r=[]
        a=1
        for i in range(len(nums)-1,-1,-1):
            r.append(a)
            a=a*nums[i]
        i=0
        a=[]
        
        j=len(r)-1
        while(i<len(l) and j>=0):
            a.append(l[i]*r[j])
            i+=1
            j-=1
        


        return a
        
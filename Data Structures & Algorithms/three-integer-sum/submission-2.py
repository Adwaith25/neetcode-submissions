class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        l1=[]
        for l in range(len(nums)):
            
            if(nums[l]!=nums[l-1] or l==0):
                i=l+1
                j=len(nums)-1
                while(i<j):
                    a=nums[i]+nums[j]+nums[l]
                    if(a>0):
                        j-=1
                    elif(a<0):
                        i+=1
                    elif(a==0):
                        l1.append([nums[l],nums[i],nums[j]])
                        i+=1
                        j-=1
                        while(i<j and nums[i]==nums[i-1]):
                            i+=1
                        
                        
        return l1



            



        
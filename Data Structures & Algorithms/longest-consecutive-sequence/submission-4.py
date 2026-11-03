class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 1
        if(len(nums)==0):
            return 0
        nums.sort()
        l=1
        a=0
        
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
               l=max(l,i-a+1)
            elif(nums[i]==nums[i-1]):
                a+=1
                continue
            else:
                a=i
        
        return l
        

        

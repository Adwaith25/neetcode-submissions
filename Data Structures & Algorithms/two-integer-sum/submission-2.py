class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if len(d)==0:
                d[nums[i]]=i
            else:
                a=target-nums[i]
                if a in d:
                    return [d[a],i]
                else:
                    d[nums[i]]=i
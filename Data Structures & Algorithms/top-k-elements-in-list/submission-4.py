class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        l=[]
        for _ in range(len(nums) + 1):
            l.append([])
        
        for i in nums:
            count[i]=1+count.get(i,0)
        for n,c in count.items():
            l[c].append(n)
        ans=[]
        a=1
        for i in range(len(nums), 0, -1):  # outer loop runs n times
            for val in l[i]:  # inner loop iterates over elements in bucket i
                ans.append(val)
                if len(ans) == k:
                    return ans
        
            
        
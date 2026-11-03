class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            a=target-numbers[i]
            if a in d:
                return [d[a]+1,i+1]
            d[numbers[i]]=i
        
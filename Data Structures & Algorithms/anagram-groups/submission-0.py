class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        if len(strs)==1:
            return [strs]
        for i in strs:
            if ("".join(sorted(i)) not in d):
                d["".join(sorted(i))]=[i]
            else:
                
                l=d["".join(sorted(i))]
                l.append(i)
                
        return (list(d.values()))
        
        
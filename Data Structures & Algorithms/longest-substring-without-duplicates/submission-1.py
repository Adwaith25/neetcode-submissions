class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        l=0
        length=0
        for r in range(len(s)):
            if(s[r] not in s1):
                s1.add(s[r])
                length=max(length,r-l+1)
            else:
                while(s[r] in s1):
                    s1.remove(s[l])
                    l+=1
                s1.add(s[r])
        return length



        
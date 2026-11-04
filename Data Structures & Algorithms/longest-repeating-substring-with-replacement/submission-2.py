class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h={}
        l=0
        r=0
        max_f=0
        max_len=0
        while(r<len(s)):
            if(s[r] not in h):
                h[s[r]]=1
                max_f=max(max_f,h[s[r]])
                if(((r-l+1)-max_f)<=k):
                    max_len=max(max_len,r-l+1)
                    r+=1
                else:
                    h[s[l]] -= 1
                    l += 1
                    r+=1
            else:
                h[s[r]]+=1
                max_f=max(max_f,h[s[r]])
                if(((r-l+1)-max_f)<=k):
                    max_len=max(max_len,r-l+1)
                    r+=1
                else:
                    h[s[l]] -= 1
                    l += 1
                    r+=1
        return max_len

        




        
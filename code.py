class Solution:
    def validanagrams(self,s,t):
        if len(s)!=len(t):
            return False
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1 
        for j in t:
            if j not in freq:
                return False 
            freq[j]-=1 
            if freq[j]<0:
                return False 
        return True 

sol=Solution()
s="anagram"
t="nagaram"
print(sol.validanagrams(s,t))

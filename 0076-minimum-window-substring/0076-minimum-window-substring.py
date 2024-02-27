class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, sub = {}, {}

        for c in t:
            target[c] = target.get(c, 0) +1
        curr_num, need_num = 0, len(target) #this is by char not nums of each char
        res_len = float("infinity")
        res_index = [-1,-1]
        l = 0
        for r in range(len(s)):
            c = s[r]
            sub[c] = sub.get(c, 0) +1
            if (c in target and target[c] == sub[c] ):
                curr_num+=1
            
            while curr_num == need_num:
                #update res
                while (r - l +1) <res_len:
                    res_len= r-l+1
                    res_index= [l,r]
                #pop from left to minix the len 
                sub[s[l]]-=1
                if s[l] in target and sub[s[l]] < target[s[l]]:
                    curr_num-=1
                l+=1
        l, r = res_index
        return s[l:r+1]     
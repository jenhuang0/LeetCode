class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # the substring need to at least pass the total char number of t. 
        # and after that we need to narrow down the substring as small as we can
        # track the index and the len of that substring 

        if t == "": 
            return ""
        target, sub = {}, {}
        
        #using dict to store the each char number in t
        for c in t:
            target[c] = target.get(c, 0) +1
        
        #using two variable to store the require char number from target, and substring char number
        req_num, curr_num = len(target), 0

        res_num = [-1,-1]
        res_len = float("infinity") 

        l = 0
        for r in range(len(s)):
            c=s[r]
            sub[c] = sub.get(c, 0) +1
            if c in target and target[c] == sub[c]:
                curr_num += 1
            #update result
            while req_num == curr_num:
                if (r-l+1) < res_len:
                    res_len = r-l+1
                    res_num = [l, r]
                #poping out from the left
                sub[s[l]] -=1
                if s[l] in target and sub[s[l]] < target[s[l]]:
                    curr_num -=1
                l+=1
        l, r = res_num
        return s[l:r+1] if res_len!=("infinity") else ""   

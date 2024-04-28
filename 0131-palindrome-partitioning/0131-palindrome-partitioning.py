class Solution:
    def partition(self, s: str) -> List[List[str]]:
        par = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                par.append(path.copy())
                return
            
            for end in range(start + 1, len(s) + 1):
                if isPalindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return par
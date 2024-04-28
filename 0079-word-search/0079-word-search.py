class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[k]:
                return False
            
            temp = board[r][c]
            board[r][c] = ''

            if backtrack(r+1, c, k+1) or backtrack(r-1, c, k+1) or backtrack(r, c+1, k+1) or backtrack(r, c-1, k+1):
                return True
            
            board[r][c] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
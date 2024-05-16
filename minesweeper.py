# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#Approach 1: BFS
from typing import List, deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board is None or len(board) == 0:
            return board
        m = len(board)
        n = len(board[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        if(board[click[0]][click[1]] == 'M'):
            board[click[0]][click[1]] = 'X'
            return board
            
        q = deque()
        q.append(click)
        board[click[0]][click[1]] = 'B'

        def countMines(r, c):
            count = 0
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if nc >=0 and nr >= 0 and nc < n and nr < m and board[nr][nc]=='M':
                    count+=1
            return count

        while q:
            curr = q.popleft()
            count = countMines(curr[0], curr[1])
            if(count == 0):
                for dir in dirs:
                    nr = curr[0] + dir[0]
                    nc = curr[1] + dir[1]
                    if nc >=0 and nr >= 0 and nc < n and nr < m and board[nr][nc]=='E':
                        q.append([nr, nc])
                        board[nr][nc] = 'B'
            else:
                board[curr[0]][curr[1]] = chr(count+ord('0'))
        
        return board
#Approach 2: DFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board is None or len(board) == 0:
            return board
        m = len(board)
        n = len(board[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        if(board[click[0]][click[1]] == 'M'):
            board[click[0]][click[1]] = 'X'
            return board
        
        def dfs(r, c):
            #logic
            board[r][c] = 'B'
            count = countMines(r, c)
            if(count == 0):
                for dir in dirs:
                    nr = r + dir[0]
                    nc = c + dir[1]
                    if nc >=0 and nr >= 0 and nc < n and nr < m and board[nr][nc]=='E':
                        dfs(nr, nc)
            else:
                board[r][c] = chr(count+ord('0'))

        def countMines(r, c):
            count = 0
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if nc >=0 and nr >= 0 and nc < n and nr < m and board[nr][nc]=='M':
                    count+=1
            return count
        
        dfs(click[0], click[1])
        return board
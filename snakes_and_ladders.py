# Time Complexity : O(n*n)
# Space Complexity : O(n*n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
from typing import List, deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [-1]*(n*n)
        even = 0
        idx = 0
        r = n-1
        c = 0

        while idx < n*n:
            if board[r][c] != -1:
                arr[idx] = board[r][c] - 1 
            idx+=1

            if (even % 2 == 0):
                c+=1
                if(c == n):
                    r-=1
                    c-=1
                    even+=1
            else:
                c-=1
                if(c == -1):
                    r-=1
                    c+=1
                    even+=1

        q = deque()
        moves = 0
        q.append(0)
        arr[0] = -2

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
               # if curr == n*n -1:
                #   return moves
                for k in range(1, 7):
                    baby = curr + k
                    if baby >= len(arr):
                        break
                    if arr[baby] != -2:
                        if arr[baby] == -1:
                            if baby == n*n - 1: return moves+1
                            q.append(baby)
                        else:
                            if arr[baby] == n*n - 1: return moves+1
                            q.append(arr[baby])
                        arr[baby] = -2
            moves+=1
        
        return -1
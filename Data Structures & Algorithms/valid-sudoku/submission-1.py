class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ver={}
        her={}
        for x in range(9):
            ver={}
            for y in range(9):
                if(board[y][x]!="."):
                    ver[board[y][x]]=ver.get(board[y][x],0)+1
            for i in ver:
                if ver[i]>=2:
                    return False
        for x in range(9):
            her={}
            for y in range(9):
                if(board[x][y]!="."):
                    her[board[x][y]]=her.get(board[x][y],0)+1
            for j in her:
                if her[j]>=2:
                    return False
        for g in range(0,9,3):
            for h in range(0,9,3):
                loop={}
                for i in range(g,g+3):
                    for j in range(h,h+3):
                        if (board[i][j]!="."):
                            loop[board[i][j]]=loop.get(board[i][j],0)+1
                for x in loop:
                    if loop[x]>=2:
                        return False
        return True


             

        


        
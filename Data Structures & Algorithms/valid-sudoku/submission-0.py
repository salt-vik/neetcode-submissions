class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        sq=[[set() for _ in range(3)]for _ in range(3)]
        for i in range(9):
            for j in range(9):
                print(i,j)
                if board[i][j]=='.':
                    continue
                else:
                    val=board[i][j]
                    if val in rows[i] or val in col[j] or val in sq[i//3][j//3]:
                        return False
                    else:
                        rows[i].add(val)
                        col[j].add(val)
                        sq[i//3][j//3].add(val)
        return True

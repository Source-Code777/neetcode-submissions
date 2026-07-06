class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen=set()
            for j in range(len(board[0])):
                value=board[i][j]
                if value==".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for j in range(len(board[0])):
            seen=set()
            for i in range(len(board)):
                value=board[i][j]
                if value==".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen=set()
                for i in range(3):
                    for j in range(3):
                        row=box_row+i
                        col=box_col+j
                        value=board[row][col]
                        if value==".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)
        return True
        
class Solution:
    def isValidSudoku(self, board):
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    # 橫的確認
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    # 直的確認
    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    # 方框內確認
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    # 確認數字
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)


s = Solution()
s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

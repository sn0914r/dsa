# Problem: valid sudoku
# Difficulty: Medium
# Link: https://leetcode.com/problems/valid-sudoku
# Date: 22-06-2026
# Approach: transform rows, columns and 3x3 sub-boxes into lists, and check each row for duplicates using a hash set
# Time: O(n2)


def isValidSudoku(board):

    def hasDuplicatesInRow(row):
        hash_set = set()

        for i in row:
            if i == ".":
                continue

            if i in hash_set:
                return True

            hash_set.add(i)

        return False

    def getColumnsAsRows(board):
        columnsAsRows = []

        for i in range(0, 9):
            column = []
            for j in range(0, 9):
                cellValue = board[j][i]
                column.append(cellValue)

            columnsAsRows.append(column)

        return columnsAsRows

    def getSubBoardsAsRows(board):
        subBoxesAsRows = []

        for boxRow in range(3):
            for boxColumn in range(3):
                singleSubBoxAsRow = []

                for i in range(3):
                    for j in range(3):
                        rowIndex = boxRow * 3 + i
                        columnIndex = boxColumn * 3 + j
                        singleSubBoxAsRow.append(board[rowIndex][columnIndex])

                subBoxesAsRows.append(singleSubBoxAsRow)

        return subBoxesAsRows

    columnsAsRows = getColumnsAsRows(board)
    subBoardsAsRows = getSubBoardsAsRows(board)

    allRows = board + columnsAsRows + subBoardsAsRows

    for row in allRows:
        isDuplicateExists = hasDuplicatesInRow(row)

        if isDuplicateExists:
            return False

    return True


testMatrix = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]

print(isValidSudoku(testMatrix))

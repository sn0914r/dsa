"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""


def getSubMatrixes(board):
    sub_matrices = []

    for box_row in list(range(0, 9, 3)):
        for box_col in list(range(0, 9, 3)):
            sub_matrix = []

            for i in list(range(box_row, box_row + 3)):
                for j in list(range(box_col, box_col + 3)):
                    sub_matrix.append(board[i][j])

            sub_matrices.append(sub_matrix)

    return sub_matrices


def getColumns(board):
    columns = []
    for i in range(9):
        col = []
        for j in range(9):
            col.append(board[j][i])
        columns.append(col)

    return columns


def checkDuplicates(arr):
    hashSet = set()

    for num in arr:
        if num == ".":
            continue

        if num in hashSet:
            return True

        hashSet.add(num)


def checkDupsForNestedArrs(nestedArr):
    for i in nestedArr:
        if checkDuplicates(i):
            return True

    return False


def validSuduko(board):
    rows = board
    columns = []
    subgridsAsArrays = getSubMatrixes(board)

    if (
        checkDupsForNestedArrs(rows)
        or checkDupsForNestedArrs(columns)
        or checkDupsForNestedArrs(subgridsAsArrays)
    ):
        return False

    return True


suduko = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(validSuduko(suduko))

suduko2 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(validSuduko(suduko2))

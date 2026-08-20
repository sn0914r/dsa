"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Approach: Hash Set - Extract rows, columns, and 3x3 sub-boxes as 1D lists, then check each list for duplicate digits using a set (ignoring '.').
"""

def is_have_dups(arr):
    seen = set()

    for n in arr:
        if n == ".":
            continue
        if n in seen:
            return True
        seen.add(n)
    
    return False

def get_columns(matrix):
    columns = []

    for col in range(9):
        single_column = []
        for row in range(9):
            single_column.append(matrix[row][col])
        
        columns.append(single_column)
    
    return columns

def get_sub_matrixes_as_arr(matrix):
    sub_matrixes = []

    for m_row_start in range(0, 9, 3):
        for m_col_start in range(0, 9, 3):
            sub_matrix = []

            for r in range(m_row_start, m_row_start+3):
                for c in range(m_col_start, m_col_start+3):
                    sub_matrix.append(matrix[r][c])
            
            sub_matrixes.append(sub_matrix)
    
    return sub_matrixes


def is_valid_suduko(matrix):
    columns = get_columns(matrix)
    sub_matrixes_as_arrs = get_sub_matrixes_as_arr(matrix)

    all_rows = matrix + sub_matrixes_as_arrs + columns
    
    
    for arr in all_rows:
        if is_have_dups(arr):
            return False
    
    return True

invalid_sudoku = [
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

valid_sudoku = [
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

print(is_valid_suduko(invalid_sudoku))  
print(is_valid_suduko(valid_sudoku))  
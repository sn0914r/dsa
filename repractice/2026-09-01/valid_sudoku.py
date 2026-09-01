# Problem: valid sudoku
# Difficulty: Medium
# Link: https://leetcode.com/problems/valid-sudoku
# Date: 22-06-2026
# Approach: transform rows, columns and 3x3 sub-boxes into lists, and check each row for duplicates using a hash set


def get_columns_as_rows(matrix):
    columns = []

    for i in range(len(matrix)):
        col = []
        for j in range(len(matrix)):
            col.append(matrix[j][i])
        columns.append(col)

    return columns

def get_submatrices_as_rows(matrix):
    submatrices = []

    for m_start_row in range(0, 9, 3):
        for m_col_start in range(0, 9, 3):
            sub_matrix = []

            for r in range(m_start_row, m_start_row + 3):
                for c in range(m_col_start, m_col_start + 3):
                    sub_matrix.append(matrix[r][c])
            
            submatrices.append(sub_matrix)
    
    return submatrices



def is_dup_in_a_row(row):
    seen = set()

    for num in row:
        if num == ".":
            continue

        if num in seen:
            return True
        seen.add(num)
    
    return False

def is_dups_in_all_rows(rows):
    for row in rows:
        if is_dup_in_a_row(row):
            return True
    return False


def is_valid_sudoku(matrix):
    all_rows = matrix + get_columns_as_rows(matrix) + get_submatrices_as_rows(matrix)
    return not is_dups_in_all_rows(all_rows)

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

print(is_valid_sudoku(invalid_sudoku))  
print(is_valid_sudoku(valid_sudoku))  
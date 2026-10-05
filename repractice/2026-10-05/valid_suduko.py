"""
Problem: valid_suduko
Approach: collect rows, columns and submatrices as rows and check if any of the rows have duplicates, if yes return False else True
"""

def contains_dups(arr):
    hashset = set()

    for e in arr:
        if e == ".":
            continue

        if e in hashset:
            return True
        
        hashset.add(e)
    
    return False

def valid_suduko(matrix):

    all_columns_as_rows = []
    for r in range(9):
        column_as_row = []
        for c in range(9):
            if matrix[c][r] != ".":
                column_as_row.append(matrix[c][r])
        
        all_columns_as_rows.append(column_as_row)
    
    all_submatrices_as_rows = []
    for r in range(0, 9,3):
        for c in range(0, 9, 3):
            submatrix = []

            for x in range(r, r + 3):
                for y in range(c, c + 3):
                    if matrix[x][y] != ".":
                        submatrix.append(matrix[x][y])
            
            all_submatrices_as_rows.append(submatrix)

    for arr in matrix + all_columns_as_rows + all_submatrices_as_rows:
        if contains_dups(arr):
            return False
    
    return True
    

m1 = [
    ["5","3",".",".","7",".",".",".","."], 
    ["6",".",".","1","9","5",".",".","."], 
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

m2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(valid_suduko(m1))
print(valid_suduko(m2))

def transpose(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    result=[]

    for c in range(columns):
        new_row=[]
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result

mat = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(mat))

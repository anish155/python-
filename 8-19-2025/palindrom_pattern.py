def pascal_concat_iter(rows):
    row = [1]
    for _ in range(rows):
        print(''.join(map(str, row)))
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]

pascal_concat_iter(5)

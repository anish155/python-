n = 4
matrix = [[0]*n for _ in range(n)]

num = 1
for d in range(2*n-1): 
    if d % 2 == 0:  
        r = 0 if d < n else d-n+1
        c = d if d < n else n-1
        while r < n and c >= 0:
            matrix[r][c] = num
            num += 1
            r += 1
            c -= 1
    else:  
        r = d if d < n else n-1
        c = 0 if d < n else d-n+1
        while r >= 0 and c < n:
            matrix[r][c] = num
            num += 1
            r -= 1
            c += 1


for row in matrix:
    print(" ".join(map(str,row)))

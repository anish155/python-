import numpy as np

matrixa=np.matrix([[1,2],[2,3],[3,4]])
matrixb=np.matrix([[4,5],[5,6],[6,7]])

print(matrixa)
print(matrixb)

matrix_sum=matrixa+matrixb
print(matrix_sum)

matrixc=np.matrix([[1,1],[2,2]])
matrixd=np.matrix([[3,3],[4,4]])

matrix_prod=matrixc*matrixd
print(matrix_prod)
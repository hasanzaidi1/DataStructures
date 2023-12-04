import numpy as np

matrix1 = np.loadtxt('matrix1.txt',dtype='i',delimiter=' ')
matrix2 = np.loadtxt('matrix2.txt',dtype='i',delimiter=' ')

r1, c1 = matrix1.shape
r2, c2 = matrix2.shape

if c1 != r2:
  print("Matrices cannot be multiplied!") 
else:
  result = np.dot(matrix1, matrix2)

  with open("result.txt",'w') as f:
    for r in result:  
      np.savetxt(f, r, fmt='%i')
  
  print("Result written to result.txt")


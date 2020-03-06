def array2d(nrow, ncol, x):
  mat = []
  for i in range(nrow):
    mat.append([])
    for j in range(ncol):
      mat[i].append(x)
  return mat
def pr_mat(mat):
  for lst in mat:
    print(lst)
mat = array2d(6, 2, 5)
pr_mat(mat)
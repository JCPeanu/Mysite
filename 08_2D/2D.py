'''lst = [1, 2, 3]
lst2 = [4, 5, 6, 9]
mat = [lst, lst2]
print(mat)
print(mat[0], mat[1])
print(mat[0][-1], mat[1][-1])
print(len(mat))
print(len(mat[0]), len(mat[1]))
mat.append([33, 44, 55])
print(mat)
mat[1].append(99)
print(mat)
mat[0] = [3.1, 4.1, 5.1]
print(mat)
mat[-1][-1] = 888
print(mat)'''
mat2 = [[5, 6, 7], [0, 9, 8], [11, 22, 33]]
def scalar(mat, num):
  for k in range(len(mat)):
    for i in range(len(mat[k])):
      mat[k][i] *= num
def scalar2(mat, num):
  for lst in mat:
    for i in range(len(lst)):
      lst[i] *= 2
scalar(mat2, 10)
print(mat2)
scalar2(mat2, 0.5)
print(mat2)

def even_list(n):
  lst = []
  for i in range(2, 2*n+1, 2):
    lst.append(i)
  return lst
print(even_list(5))
def desc_list(n):
  lst = []
  for i in range(n, 0, -1):
    lst.append(i)
  return lst
print(desc_list(5))

import random
def random_list(n):
  lst = []
  for i in range(n):
    lst.append(random.random())
  return lst
print(random_list(5))

def rand_list(n, a, b):
  lst = []
  for i in range(n):
    lst.append(random.randint(a, b))
  return(lst)
print(rand_list(5,1,50))
def square_list(nums):
  return [x*x for x in nums]
print(square_list([3,4,5]))

def abs_list(nums,x):
  return [a for a in nums if abs(a) < x]
print(abs_list([3,4,-1,-2,2,7,1],3))

import math
def pi_list(n):
  return [round(math.pi,i) for i in range(1, n+1)]
print(pi_list(5))

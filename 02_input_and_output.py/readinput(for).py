import math
def square_root():
  num = int(input())
  j = 1
  for i in range(num):
    line = int(input())
    r = round(math.sqrt(line),3)
    fmt = 'input{}: {} sqrt{}: {}'.format(j,line,j,r)
    print(fmt)
    j += 1

square_root()
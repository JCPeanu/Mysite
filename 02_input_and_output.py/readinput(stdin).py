import sys
def square():
  i = 1
  for line in sys.stdin:
    line = line.strip()
    num = int(line)
    fmt = 'input{}: {} square{}: {}'.format(i,num,i,num**2)
    print(fmt)
    i += 1
square()
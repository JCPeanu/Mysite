import sys
def table():
  for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    '''
    fmt = '{:10}{:>7}{:>7}{:>7}{:>7}'.format(tokens[0],tokens[1],
    tokens[2],tokens[3],tokens[4])
    '''
    for x in tokens:
      print(x.ljust(10), end='')
    total = 0
    for j in range(1,len(tokens)):
      total += int(tokens[j])
    print('total:', total)
table()
    
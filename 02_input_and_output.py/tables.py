import sys
def table():
  total_age = 0
  nline = 0
  total_h = 0
  total_w = 0
  for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    name = tokens[0]
    age = int(tokens[1])
    h = float(tokens[2])
    w = float(tokens[3])
    fmt = '{:6}{:3}{:7}{:5}'.format(name,age,h,w)
    print(fmt)
    nline += 1
    total_age += age
    total_h += h
    total_w += w
  print('avg age:',total_age/nline)
  print('avg height:',round(total_h/nline,2))
  print('avg weight:',round(total_w/nline,2))
table()
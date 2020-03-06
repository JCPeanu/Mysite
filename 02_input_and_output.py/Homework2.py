import sys
def homework():
  for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    name, done, total = tokens[0], int(tokens[1]), int(tokens[2])
    rate = done/total
    per = round(rate*100)
    nstar = round(20 * rate)
    npipe = 20 - nstar
    fmt = '{:10}{:3}% {:}{:}'.format(name,per, nstar*'*', npipe*'|')
    print(fmt)
homework()
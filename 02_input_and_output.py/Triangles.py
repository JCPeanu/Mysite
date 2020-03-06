import sys
def triangles():  
  for line in sys.stdin:
    num = str(line)
    mal = line[2]
    tok = str(num[0])
    tokens = int(tok)
    sum = 0
    for i in range(tokens):
      sum += 1
      tri = mal * sum
      print(tri)
triangles()
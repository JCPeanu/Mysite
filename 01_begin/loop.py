def prNum(n):
  for i in range(0,n+1):
      print(i,end = ' ')
  print("")
prNum(4)
def prRange(a,b):
  for i in range(a, b):
      print(a, end=' ')
      a = a+1
  print("")
prRange(5,10)
def prOdds(n):
  o = 1
  for i in range (0, n):
   print(o,end=' ')
   o+=2
  print("")
prOdds(5)

def prOdds2(n):
  for i in range(1, 2*n, 2):
   print(i,end=' ')
  print("") 
prOdds2(4)
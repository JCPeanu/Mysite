def line(m, n, ch = '*'):
  for i in range(n):
    print(ch, end='')
  
def frame(m, n, ch='*'):
  line(m,n,ch)
  print()
  for j in range(m-2):
    print(ch, end='')
    line(m,n-2,ch=' ')
    print(ch)
  line(m,n,ch)
  print()
frame(5,6,"#")
frame(7,15,'@')
def frame2(m, n, ch='*'):
  print(ch*n)
  for i in range(m-2):
    print(ch, ' '*(n-2), ch, sep='')
  print(ch*n)
frame2(5,6,"_")

def square_numbers(n):
  i = 1
  j = 1
  while i < n:
    if j*j < n:
      print(j*j, end=' ')
      j += 1
      i += j
    else:
      i+=1
  print()
square_numbers(25)
def square(n):
  i = 1
  while i**2 < n:
    print(i**2, end = ' ')
    i += 1
square(25)
import math
def square2(n):
  j = 1
  sr = math.floor(n**0.5)
  for i in range(j,sr+1):
    if i**2 < n:
      print(i**2,end=' ')
  print()
square2(100)

def pr_digits(n):
  i = 0
  while i < n:
    print(n%10, end = '')
    n = n//10
  print("")
pr_digits(123059234)

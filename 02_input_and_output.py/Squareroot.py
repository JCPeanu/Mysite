def pr_roots(x,k):
  sqr = x**0.5
  for i in range(1,k+1):
    num = round(sqr,i)
    s = str(num)
    print(s.rjust(8), end=' ')
  print()
pr_roots(3,5)
pr_roots(5,3)

print('----------------------------------------')

def pr_table(n,k):
  for i in range(1,n+1):
    pr_roots(i,k)
pr_table(5,5)
  
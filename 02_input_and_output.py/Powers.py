def pr_powers(x,k):
  for i in range(1,k+1):
    po = x**i
    s = str(po)
    print(s.rjust(4), end=' ')
  print()
pr_powers(3,5)

print('----------------------------------------')

def pr_table(n,k):
  for i in range(1,n+1):
    pr_powers(i,k)
pr_table(5,5)
  
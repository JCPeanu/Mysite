lst = []
def list1(n):
  return list(range(1,n+1))
print(list1(5))

def list2(a,b):
  return list(range(a, b+1))
print(list2(2,6))

def list3(a,b):
  return list(range(a, b+1,2))
print(list3(1,9))

def list4(a,b):
  return list(range(a, b-1, -1))
print(list4(5,1))
def tables():
  cnt = int(input())
  for k in range(cnt):
    line = input()
    tokens = int(line)
    for i in range(1, tokens+1):
      for j in range(1, tokens+1):
        x = i*j
        print(str(x).rjust(3), end='')
      print()
    
tables()
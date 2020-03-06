def compute():
  cnt = int(input())
  for i in range(cnt):
    line = input()
    tokens = line.split()
    total = 0
    #for j in range(len(tokens)):
    for j in tokens:
      #total += int(tokens[j])
      total += int(j)
    avg = round(total/len(tokens),2)
    print("total:",total,"avg:",avg) 
compute()
def rect(m,n,ch):
    for i in range(0,m):
        for j in range(0,n):
            print(ch,end=' ')
        print("")
rect(5,5,"#")
def rect2(m,n,ch):
  i=0
  while i<m:
   j=0
   while j<n:
     print(ch,end=' ')
     j+=1
   print("")
   i+=1
rect2(3,5,'#')
def rect3(m,n,ch):
    line = (ch+' ')*n
    for i in range(m):
        print(line)
rect3(3,5,"#")
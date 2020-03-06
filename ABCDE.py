def a():
  for i in range(1,100000):
    x = 100000 + i
    ones = x%10
    tens = (x%100)/10
    hundreds = (x%1000)/100
    thousands = (x%10000)/1000
    tenthousands = (x%100000)/10000
    y = tenthousands * 10000 + thousands * 1000 + hundreds * 100 + tens * 10 + ones * 1
    z = ones * 10000 + tens * 1000 + hundreds * 100 + thousands * 10 + tenthousands * 1
    if y * 4 == z and y * 4 ≠ 0:
      print(y,"* 4 = ",z)
a()

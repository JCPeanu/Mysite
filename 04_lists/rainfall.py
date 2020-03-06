names = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 
'SEP', 'OCT', 'NOV', 'DEC']
rain = [35.1, 44.2, 51.5, 76.3, 45.6, 112.4, 135.1, 14.2, 61.5, 
79.3, 33.6, 102.3]
def year_avg(arr):
  total = 0
  for x in arr:
    total += x
  print('year avg:',round(total / len(arr),2),'mm',sep='')
def spring_avg(arr):
  total = 0
  for x in arr[:3]:
    total += x
  print('spring avg:',round(total/len(arr[:3]),2),'mm',sep='')
def summer_avg(arr):
  total = 0
  for x in arr[3:7]:
    total += x
  print('summer avg:',round(total/len(arr[3:7]),2),'mm',sep='')
def autumn_avg(arr):
  total = 0
  for x in arr[7:10]:
    total += x
  print('autumn avg:',round(total/len(arr[7:10]),2),'mm',sep='')
def winter_avg(arr):
  total = 0
  for x in arr[10:]:
    total += x
  print('winter avg:',round(total/len(arr[10:]),2),'mm',sep='')
def odd_avg(arr):
  total = 0
  for x in arr[0::2]:
    total += x
  print('odd avg:',round(total/len(arr[0::2]),2),'mm',sep='')
def even_avg(arr):
  total = 0
  for x in arr[1::2]:
    total += x
  print('even avg:',round(total/len(arr[1::2]),2),'mm',sep='')
def list():
  year_avg(rain)
  spring_avg(rain)
  summer_avg(rain)
  autumn_avg(rain)
  winter_avg(rain)
  odd_avg(rain)
  even_avg(rain)
list()

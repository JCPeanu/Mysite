def ticket(age):
    if (age<15):
      print("children")
    elif (age<64):
      print("adults")
    else:
      print("seniors")
def test():
  ticket(10)
  ticket(15)
  ticket(20)
  ticket(65)
  ticket(80)
test()
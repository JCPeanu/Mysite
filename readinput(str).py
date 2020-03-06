def words():
  line = input()
  tokens = line.split()
  for token in tokens:
    print(token,len(token))
words()
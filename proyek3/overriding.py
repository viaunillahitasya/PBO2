class fisika:
  def add(self, a, b):
     return a + b
  def add(self, a, b, c=0):
     return a + b + c

fis = fisika()
B = fis.add(9, 7, 5)
print(B)
mut = fisika()
C = mut.add(7,3)
print(C)
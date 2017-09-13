import random
from itertools import *
x = input("enter x:")
y = input("enter y:")
N = int(y)
people = [i+1 for i in range(N)]
mapping = []
popList = {}
for p in people:
  popList[p] = int(x)

for p in people:
  M = int(x)
  #peopleList = [i+1 for i in range(N)]
  while (M>0):
    r = random.randint(1,N)
    if p!=r and popList[r]>0:
      mapping.append((p,r))
      print popList[r]
      popList[r] = popList[r]-1
      M = M-1
print(popList)
print(mapping) 

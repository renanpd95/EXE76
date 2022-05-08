import random


for i in range(20):

  n = random.randint(0,20)
  
  for x in range(20):
    mult = n*x
    print(n,"x",x,"=",mult)
#DICE ROLLING SIMULATOR

import random
print("welcome to dice rolling simulator")
print("to roll the number enter Y and to end enter N")
t=input()
while(t=="Y"):
   print(random.randint(1,6))
   t=input()
   if t=="N":
       break


print("dice rolling simulator ends")


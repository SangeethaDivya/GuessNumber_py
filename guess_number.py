import time
import random
print("welcome!!!\u1F64F")
time.sleep(3)
print("Lets start!!")
lb=int(input("enter lower limit"))
ub=int(input("enter upper limit"))
comp=random.randint(lb,ub)
chances=lb+ub//(ub//2)
time.sleep(2)
print("you have {} chances to guess the number".format(chances))
for i in range(chances,0,-1):
    user=int(input("Guess: "))
    if user==comp:
        print("you win!! in {} chances".format(chances-i))
        break
    if i==0:
        print("you losse!!")

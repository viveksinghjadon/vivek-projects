import random
comp=random.randint(0,2)
user=int(input("0 for snake, 1 for water, 2 for gun :"))

if(user==0 and comp==1):
    print("you won")
    print(comp)
    
elif(user==1 and comp==2):
    print("you won")
    print(comp)
elif(user==2 and comp==0):
    print("you won")
    print(comp)
elif(user==comp):
    print("Draw")
    print(comp)
else:
    print("you lose")
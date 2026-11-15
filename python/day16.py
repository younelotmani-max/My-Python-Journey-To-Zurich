y=[1,2,3,4,5,]
if all(y):
    print("good")
else :
    print("try another time")    

y=[ 1,0, 0,[]]
if any(y):
    print("great")
else :
    print("Bad") 

nuy=[1,2,3,4,5,]
if all(y):
    print("Mzyan aw9 mzn")
else :
    print("sir traj3 had drss mzn a zaml")

num=276283
print(bin(num))

tfu="nta ah nta"
print(id(tfu))

l=[1500, 3200, 500, 4800]
print(sum(l))

range()
print(list(range(0,40,2)))

rate=[10, 85, 40, 95, 20, 75]
ratedanger=filter(lambda rte : rte>=70  , rate)
for x in ratedanger :
    print(x)

from functools import reduce 

def mynumber(num1,num2):

    return num1, num2

numbers=[2, 3, 4, 5]
resultat=reduce( lambda num1,num2 : num1+num2,numbers)
print(resultat)

blacklist=["Younes", "Ahlam", "Karim"]
listwihtcounter=enumerate(blacklist)

for ana,nta in listwihtcounter:
    print(f"{ana} - {nta}")

from random import randint
print(f"code pin de verification account NexusBank: {randint(1000,900000)}")

import pyfiglet
print(pyfiglet.figlet_format("NexusBank"))


def show_engineur(name, *langs, **projets):
    print(f"Hello {name}")
    for lougha in langs:
        print(f"- {lougha}")
    for key, value in projets.items():
        print(f"and {key}: {value}")

show_engineur("Younes", "python", "js", site="youn.express", ai="google ai")

salary=15000
def upgrade_salary():
    global salary  
    salary+=5000 
   
upgrade_salary()
print(salary)

def salam(hello):
    print("Hello")
    if hello == 6:
        return
    print(hello)
    salam(hello+1)
salam(1)    

def num(numbers):
   
    if numbers==11:
        return
    print(numbers)
    num(numbers+1)
num(1) 
   
def countdown(n):
    if n == 0:
        print("Blast Off")
        return
    else:
        print(n)
        countdown(n-1)
countdown(5)    

def say_hello(salary): return f"Younr salry is {salary}"
calc_tax = lambda salary: salary * 0.2  
print(calc_tax(15000))

mydata=open(r"C:\Users\__uness\OneDrive\Documents\data.txt")
print(mydata.read())
print(mydata.close())

room_admins=open(r"C:\Users\__uness\OneDrive\Documents\admins_db.txt" ,"w")
room_admins.write("Younes\n")
room_admins.write("Ahlam")
room_admins.close()

test=open(r"C:\Users\__uness\OneDrive\Documents\test_delete.txt" ,"w")
test.close()
import os
os.remove(r"C:\Users\__uness\OneDrive\Documents\test_delete.txt")









        
       
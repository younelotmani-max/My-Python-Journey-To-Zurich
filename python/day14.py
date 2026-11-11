mynumbers=[1,2,3,4,6,8,9,13,15,16,29]
for number in mynumbers :
    if number==6 :
        continue
     
    if number==16:
        break
    print(number)

for_country={
    "maroc":"rabat",
    "france":"paris",
    "italy":"roma"
}

for capital in for_country.items():
    print(capital)

def say_hello():
    return "Welcome to Google Zurich AI!"
database_for_engineur=say_hello()
print(database_for_engineur)

def add_bonus(name, salary):
   print(f"heelo {name} , your salary is {salary + 5000}")
add_bonus("Younes", 10000 )

def print_admins(*admins):
   
    for engineur in admins:
        print(engineur)

print_admins("Younes","Ahlam","Kamal","aya")        
        





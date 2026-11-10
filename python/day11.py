#age = 19

#if age >= 18: 
   # print("Access Granted")

#if age <= 18:
   # print("Access Denied")   


age = input("PLEASE WRITE YOUR AGE ? ").strip()
unit= input("Please chose : Months , Weeks , Days , hours , minutes , secondes : ").strip().lower()

months= int(age)*12
weeks= months*4
days=int(weeks)*365
hours = days*24
minutes = hours*60
secondes = minutes*60

if unit == "months"or unit=="m":
    print("You chose months")
    print(f"your age  is {months} months .")

elif unit == "weeks"or unit=="w":
    print("You chose weeks")
    print(f"your age  is {weeks} weeks .")    

elif unit == "days"or unit=="d":
    print("You chose days")
    print(f"your age  is {days} days .")

elif unit== "hours"or unit=="h":
    print("You chose hours")
    print(f"your age is {hours} hours .")

elif unit== "minutes"or unit=="mi":
    print("You chose minutes")
    print(f"your age is {minutes} minutes .")

elif unit== "secondes"or unit=="s":
    print("You chose secondes")
    print(f"your age is {secondes} secondes .")


languages=["Python", "C++", "Java"]
languages_tow=["html"]
languages_one=input("Your languages coding ? ")
if languages == ["Python", "C++", "Java"]:
     print("Accepted for AI")

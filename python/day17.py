smiyat=["Younes", "Ahlam", "Karim"]
salaire=[50000, 120000, 3000]
for hbiba , bb in zip(smiyat,salaire):
    print(hbiba  , bb)

from PIL import image
my_image=image.open(r"C:\Users\__uness\OneDrive\Images\Gemini_Generated_Image_mr0g7vmr0g7vmr0g.jfif")
my_image.show()

def numbers(number):
    """hada akhouya 3amaliya ms makat3tich jawab kadir ghir 2*2 sf fhmtini bon courage"""
    print(f"number is {number}*2")
numbers(2)    
help(numbers)


amount=input("How much u whant deposit in your account : ")
x=-10
if x <= 0:
    raise ValueError("Amount must be greater than zero!")

else :
    print("Crongulation")

try:
    number=int(input("your age please : "))
    print("thank you ")
except : 
    print("Error! Please enter numbers only")      

try:
    NUMBER = float(input("write a number : "))
    print(f"the result is {NUMBER / 100}")
except ValueError:
    print("no no error")
except  :
    print("BIG ERROR")           

def add_money(balance, amount):
    new_balance = balance + amount
    return new_balance

balance = 500
amount = float(input("How much to deposit : "))
balance = add_money(balance, amount)
print(f"New balance : {balance}")


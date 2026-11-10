fname = input("waths your first name ? ")
lname = input("and your last name ? ")
themail= input("what your email ? ")
age= int(input("What your Age ? ").strip())
theusername = themail[ :themail.index("@")]
thewebsite = themail[ themail.index("@") + 1 : ]
print(f"Hello {fname.strip().capitalize()} {lname.strip().capitalize()} how can i help u today ?") 
print("="*100)
print("ALL OF YOUR INFORMATIONS : ")
months = age*12 
weeks = months*4
days = age*365
hours = days*24
minutes = hours*60
secondes = minutes*60
print(f"your age with months : {months} \nwith weeks : {weeks} \nwith days : {days} \nwith hours : {hours} \nwith minutes : {minutes} \nwith secondes : {secondes} ")
print(f"Your name is : {fname.strip()} \nyour username is : {theusername.strip()} \nyour gmail is : {themail.strip()} \nyour name f domaine is : {thewebsite}")

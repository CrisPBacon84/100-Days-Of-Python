bill=0
print("welcome to rollercoster")
height = int(input("write your height in cm "))
if height>80:
    print("you can ride the rollercoster")
    age= int(input("What is your age "))
    if age<12:
        bill=5
        print("You have to pay 5$")
    elif age<=18:
        bill=12
        print("you have to pay 12$.")  
    else:
        bill=20
        print("you have to pay 20$")  
    Wants_photo= input("You want a photo or not? Type Y for Yes and N for No ")
    if Wants_photo.upper()== "Y":
      bill+=3
      print(f"your total bill is {bill}")      
else:
    print("you have to grow taller before you ride")    
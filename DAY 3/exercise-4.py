bill=0
print("welcome to python pizza Deliveries! ")
size = input("what size do you want? S, M OR L, ")
add_pepperoni = input("Do you want to add pepperoni? Type 'Y' for yes and 'N' for no")
extra_cheese = input("DO you want extra cheese? Type Y or N ")
if size=="S":
    bill= 15
elif size== "M":
    bill=20 
elif size== "L":
    bill=25
if add_pepperoni =="Y":
    if size=="S":
      bill+=2
    else:
        bill+=3
if extra_cheese== "Y":
    bill+=3
print(f"Your total bill is {bill}")    
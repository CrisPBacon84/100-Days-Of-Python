height= float(input("what is your height in m "))
weight = float(input("what is your weight in kg "))
bmi = height/weight**2
if bmi<=18.8:
    print(f" your bmi is {bmi} You are under weight")
elif bmi <25:
    print(f" your bmi is {bmi} You have normal weight")
elif bmi<30:
     print(f" your bmi is {bmi} You are overweight" )
elif bmi<35:
        print(f" your bmi is {bmi} You are obese")
else:
    print("You are clinically obese")        
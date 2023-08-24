print("welocome to treasure island")
print("your job is to find the treasure")
Left_right = input("Where do you want to go left or right? ")
if Left_right=="right":
    print("congratulations you lost the game ")
elif Left_right== "left":
    swim=input("Boat will come shortly You want to wait or swim? ")
    if swim == "swim":
        print("you have been eaten by the shark! Game Over")
    elif swim == "wait":
        door = input("which door you want to go with red, blue or yellow? ")
        if door=="red":
            print("Sorry You died! Game Over")         
        elif door == "blue":
            print("Sorry you died! Game Over")    
        elif door == "yellow":    
            print("Congratulations You Win!")
import random
names_people= input("Give me everybody names separated by comma ")
names= names_people.split(",")
random_number = random.randrange(1, 10)
print(names[random_number - 1], "is going to pay the bill")


import random

def coin_toss():
    result = random.choice(['Heads', 'Tails'])
    return result

if __name__ == "__main__":
    print("Welcome to the Coin Toss Simulator!")
    num_tosses = int(input("How many times do you want to toss the coin? "))
    
    for _ in range(num_tosses):
        outcome = coin_toss()
        print(outcome)

"""import random
random_side =random.randint(0,1)        
if random==1:
    print("Heads")
else:
    print("Tails"""")"""     

import random

print(random.randint(1000,9999))
print(random.choice([1,2,10,"tops","python",100]))

num=random.randint(1,20)

while True:
    guess=int(input("Guess A Number Between 1 to 20 :"))

    if guess==num:
        print("You Guess A Curect Number")
    elif guess>num:
        print("You Guess A Greater Number")
    elif guess<num:
        print("You Gurss A Smaller Number")
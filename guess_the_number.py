import random
number=random.randrange(0,100)
user=input("Choose difficulty easy or hard : ")
if user=="easy":
    attempts=10
else:
    attempts=5
print(f"You have {attempts} attempts to guess the number")
while attempts>0:
    user_number=int(input("Make a guess : "))
    if number>user_number:
        print("Too low")
    elif number<user_number:
        print("Too high")
    else:
        print("You got it right")
        exit()
    attempts=attempts-1
    print(f"{attempts} attempts left")
    

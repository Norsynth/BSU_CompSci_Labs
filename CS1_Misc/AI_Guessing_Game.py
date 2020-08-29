import random
myNumber = int(input("Enter number for Computer to guess between 1 and 100: "))
guess = 0
attempts = 1
min = 1
max = 100

if 1 <= myNumber <=100:
  
    while guess != myNumber:
        guess = int(((min + max)/2))
        print(guess,"?")
        

        if guess < myNumber:
            print("Higher")
            min  = guess
            attempts += 1
        elif guess > myNumber:
            print("Lower")
            max = guess

            attempts += 1

        else: guess = myNumber;

    print("The Computer needed", attempts, "attempts")

elif myNumber < 1 or myNumber >100:
  print("Please enter a number between 1 and 100!")

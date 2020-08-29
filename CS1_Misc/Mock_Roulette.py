'''
[4ex7.py]
This program is a mock gambling game, where you choose the amount to bet,
and receive $4 for every 7 rolled. The game costs $1 a turn.

'''

import random


bank = int(input("Enter starting wager $"))
roll_again = input("Roll the dice? (yes/no):")
roll = 1
maxBank = bank
    
while roll_again == "yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("(",dice1,")","(",dice2,")")
        if dice1+dice2 == 7:
            print("You win!")
            bank += 4
            roll += 1
            if bank > maxBank:
                maxBank = bank
            print("Your total is $",bank,)
            roll_again = input("Roll the dice again? (yes/no)")
            

        
        elif dice1+dice2 != 7: 
            bank -= 1
            if bank == 0:
                        print("You lost your money :(")
                        print("It took",roll,"rolls...")
                        print("Your highest pot was $",maxBank,)
                        break
            elif bank != 0:
                print("Your total is $",bank,)
                roll += 1
                roll_again = input("Roll the dice again? (yes/no)")

else:
    print("Thanks for playing! Your total is $",bank)


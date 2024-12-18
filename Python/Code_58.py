'''
Q.58. Guess the number give three attempts
'''
import random as Rm

print( "--------------------------------------------------" )
print( "HELLO AND WELCOME TO THE NUMBER GUSSING GAME " )
print( "--------------------------------------------------" )

Start = int( input( " Enter the start number: " ) )
End = int( input( " Enter the end number: " ) )

Chances = 3

Num_to_guess = Rm.randrange(Start,End)

print("You have only 3 chances to guess it correctly number. ")
print("````````````````````````````````````````````````````````")

for Attempt in range(1,100):
    Guess = int( input( " Enter your number: " ) )
    
    if Guess == Num_to_guess:
        print( " Congratulations you have guessed correct number. " )
        break
    elif Guess < Num_to_guess:
        print( " Your guessed number is lower number. " )
    elif Guess > Num_to_guess:
        print( " Your guessed number is higher number. " )
    else:
        print( " Oops better luck next time. " )
'''
Q26. Write a program to print the random number by using random module.
'''

import random as Ra

for K in range( 1, 11 ):
    Temp = Ra.randint(20,100)
    print( f" Reading {K} \n Temperature = {Temp} " )
    
    if Temp > 70:
        print( " Danger High Temperature. " )
        break
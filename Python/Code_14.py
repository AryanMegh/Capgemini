'''
Q14. Write a program to accept a number from user and check
wheather it is divisible by 3 and 5.
'''

num = int( input( " Enter numbmer: " ) )

if num % 3 == 0 or num % 5 == 0:
    print( " The number is divisble by 3 and 5 " )
else:
    print( " The number isn't divisble by 3 and 5 " )
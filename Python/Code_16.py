'''
Q16. Write a program o accept percentage from user and make a decision about his grade
'''
Data = int( input( " Enter percentage of the user: " ) )

if Data >= 99:
    Percentage = 'O'
    print( Percentage, " grade " )
elif Data >= 70:
    Percentage = 'A'
    print( Percentage, " grade " )
elif Data <= 69:
    Percentage = 'B'
    print( Percentage, " grade " )
elif Data <= 59:
    Percentage = 'C'
    print( Percentage, " grade " )
elif Data <= 40:
    Percentage = 'D'
    print( Percentage, " grade " )
else:
    print( " you failed " )
'''
Q1) Write a program to find greatest among two numbers?
'''

Num1 = int( input( " Enter first number: " ) )
Num2 = int( input( " Enter second number: " ) )

if Num1 == Num2:
    print( " Two nummbers are equal. " )
elif Num2 > Num1:
    print( Num2, " is greater than ", Num1 )
else:
    print( Num1, " is greatest number. " )
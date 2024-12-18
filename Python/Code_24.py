'''
Q24. Write a program to print the factorial number by taking input from user.
'''

Num = int( input( " Enter number: " ) )

for I in range(0, Num):
    Fact = Fact * I

print( " The factorial of number is: ", Fact )
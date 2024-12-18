'''
Q9. Write a program to print the simple interest and accept
principal amount, rate of interest and time period.
'''

p = int( input( " Enter principal amount: "  ) )
r = int( input( " Enter rate: " ) )
t = int( input( " Enter time period: " ) )

si = (p * r * t)/100

print( " The Simple interest = ", si )
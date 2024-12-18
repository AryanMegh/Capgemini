'''
Q3. Write a program to print the greatest number from three numbers?
'''
N1 = int( iput( " Enter first number: " ) )
N2 = int( iput( " Enter second number: " ) )
N3 = int( iput( " Enter third number: " ) )

if N2 > N1:
    print( " The greatest number is: ", N2 );
elif(N3 > N2):
    print( " The greatest nubmer is: ", N3 );
else:
    print( " The greatest number is: ", N1 );

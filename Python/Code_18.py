'''
Q18. Write a program to print the multiplication number from user.
'''
Num = int( input( " Enter number: "  ) )

for I in range(1,12):
    Ans = Num * I
    print( Num, " * ", I, "=", Ans )
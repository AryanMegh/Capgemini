#Write a program to generate a table of a number
Num = int( input( " Enter number: " ) )

I = 1

while(I <= 20):
    Ans = Num * I
    print( Num, "*", I, "=", Ans )
    I += 1
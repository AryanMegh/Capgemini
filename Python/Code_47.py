'''
Q47. Write a program to print the sum of digits?
'''

Num = int( input( " Enter number: " ) )

Sum = 0

while Num > 0:
    Rem = Num % 10
    Sum = Sum + Rem
    Num = Num//10

print( " Sum = ", Sum )

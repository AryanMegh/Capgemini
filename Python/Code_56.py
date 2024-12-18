'''
Q56. Write a program to print the different patterns?
'''

#1: Number increasing pyramid
N = int( input( " Enter the total size of pattern: " ) )

for I in range(1,N):
    for J in range(I):
        print( I, end="" )
    print()

print( "-------------------" )
#2. Square Hallow pattern

N = int( input( " Enter the total size of pattern: " ) )

for I in range(0, N):
    for K in range(I):
        if I == 0 or K == 0 or I == N - 1 or K == N - 1:
            print( "*", end="" )
        else:
            print( "  " )
    print( "", end="" )
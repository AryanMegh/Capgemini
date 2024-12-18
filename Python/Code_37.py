'''
Q37. Write a program to print the largest element from a list.
'''

Data = []

Num = int( input( " Enter the range of the number: " ) )

for K in range(0,Num):
    Ele = int( input( " Enter elements = " ) )
    Data.append( Ele )
    
print( " Data in the list: ", Data )

for A in range( 0 , Num ):
    for K in range( A + 1, Num ):
        if Data[K] > Data[A]:
            Temp = Data[A]
            Data[A] = Data[K]
            Data[K] = Temp
        else:
            print( " !Error. " )

print( " The second largest number is: ", Data )
print( " The second largest number is: ", Data[1] )
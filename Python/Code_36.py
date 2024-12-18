'''
Q36. Write a program to print the data in the list using loop
'''
Data = []

Num = int( input( " Enter the range of the number: " ) )

for K in range(0,Num):
    Ele = int( input( " Enter elements = " ) )
    Data.append( Ele )
    
print( " Data in the list: " )
for A in range( len(Data) ):
    print( A )
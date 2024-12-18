#Q34. Write a program to find the maximum number from a list.

Mark = []

Num = int( input( " Enter the range of the number: " ) )

for K in range(0,Num):
    Ele = int( input( " Enter elements = " ) )
    Mark.append( Ele )
    
print( " Data in the list: ", Mark )
print( " The minimum number from the list is: ", max(Mark) )
#Write a program to accept marks of three subject and print its sum and avg

M1 = int( input( " Enter marks of subject 1: " ) )
M2 = int( input( " \n Enter marks of subject 2: " ) )
M3 = int( input( " \n Enter marks of subject 3: " ) )

Sum = M1 + M2 + M3
Avg = ( M1 + M2 + M3 ) / 3

print( " \n Total of three subject = ", Sum )
print( " \n Average of three marks = ", Avg )
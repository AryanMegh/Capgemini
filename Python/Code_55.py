'''
Q54. Write a program to print the total length of the set?
'''

Ele_A = input( " Enter elements in the first set: " )
Elelist_A = Ele_A.split( "," )
Set_A = set( Elelist_A )

print( " The data in the first set: ", Set_A )

Ele_B = input( " Enter elements in the second set: " )
Elelist_B = Ele_B.split( "," )
Set_B = set( Elelist_B )

print( " The data in the second set: ", Set_B )

print( " The data type of first set is: ", type(Set_A) )
print( " The data type of second set is: ", type(Set_B) )

Combine_data = Set_A.union(Set_B)

print( " Combined data is: ", Combine_data )

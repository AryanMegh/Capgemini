'''
Q52. Write a program to find the symentric difference between two set
'''

Set_A = {1,2,3,4,5,6,7,8,9,10,11,12}
Set_B = {13,14,15,16,17,18,19,20,21,22,23,24,25,26}

print( " Data in the first set is: ", Set_A, " \n Data in the second set is: ", Set_B )
print( " Data type of set 1 is: ", type(Set_A), "\n Data type of set 2 is:", type(Set_B) )

Res = Set_A ^ Set_B

print( " The symentric difference between two set is: ", Res )




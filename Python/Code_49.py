'''
Q49. Write a program to find the intersection between two set using intersect method.
'''

Set1 = {1,2,3,4,5,6,7,8,9,10,11,12}
Set2 = {13,14,15,16,17,18,19,20,21,22,23,24,25,26}

print( " Data in the first set is: ", Set1, " \n Data in the second set is: ", Set2 )
print( " Data type of set 1 is: ", type(Set1), "\n Data type of set 2 is:", type(Set2) )

Combined_set = Set1 & Set2

print( " Intersection between two set is: ", Combined_set )


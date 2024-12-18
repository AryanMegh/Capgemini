'''
Q21. Write a program to generate even number between 1 and 20 from user?
'''

S_value = int( input( " Enter the strating range of the number: " ) )
End_value = int( input( " Enter the ending range of the number: " ) )

for K in range(S_value,End_value+1):
    if K % 2 == 0:
        print( K )
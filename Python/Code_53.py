'''
Q53. Write a program to reverse a dictonary by taking inputt from user
'''
Dict = {}

Num = int( input( " Enter range of the dictonary: " ) )

for I in range(0,Num):
    Key = int( input( " Enter key: " ) )
    Value = input( " Enter value: " )
    Dict[Key] = Value

print( " The Data in the dictonary: ", Dict )

Reverse_dict = dict( reversed( Dict.items() ) )

print( " The reverse of number is: ", Reverse_dict )

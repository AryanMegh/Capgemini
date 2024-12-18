'''
Q48. Write a program to check wheather a number is an armstrong number.
'''
def Armstrong_num(Num):
    Str_num = str(Num)
    Num_digit = len(Str_num)
    Sum_of_number = sum( int(Digit) ** Num_digit for Digit in Str_num)
    return Num == Sum_of_number

Num = int( input( " Enter number: " ) )

if Armstrong_num(Num):
    print( Num, "is an armstrong number" )
else:
    print( Num, " is not an armstrong number. " )

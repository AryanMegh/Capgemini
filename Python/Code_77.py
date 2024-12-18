def Find_occurance(Main_string, Substring):
    Index = Main_string.find( Substring )
    return Index

Main_string = []
Substring = []

R1 = int( input( " Enter range of the main string: " ) )
R2 = int( input( " Enter range of the substring: " ) )

for I in range(0, R1):
    Ele1 = int( input( " Enter elements: " ) )
    Main_string.append(R1)

print( " Data in first string is: ", Main_string )

for I in range(0, R1):
    Ele2 = int( input( " Enter element of the second string: " ) )
    Substring.append(R2)

print( " Data in the seccond string is: ", Substring )


Index = Find_occurance(Main_string, Substring)


if Index != -1:
    print( f" The first occurrence of '{Substring}' is at index {Index}." )
else:
    print( f" The substring '{Substring}' was not found in the main string. " )

Str = input( " Enter data: " )

Result = ""

Vowel = "a,e,i,o,u,A,E,I,O,U"

for I in range( len( Str ) ):
    if Str[I] in Vowel:
        Result = Result + Str[I]

print( " String data: ", Str )
print( " After removing vowels: ", Result )

#Pattern-1: Rights hall pattern
Rd = 5

for I in range(1 , Rd + 1): 
    for J in range(1 , I):
         print("*", end="")
    print()  

print( "-------------------------" )

#Pattern-2: Reverse-rights hall pattern
for I in range(1 , Rd + 1): 
    for J in range(1 , Rd - I + 1 + 1):
         print("*", end="")
    print()
    
print( "-------------------------" )
#Pattern-3: Left half pyramid

N = 5

for I in range(1, N + 1):
	for J in range(1, N - I + 1):
		print(" ", end="")
		
	for J in range(1, I + 1):
		print("*", end="")
	print()
 
print( "-----------------------------" ) 

#Pattern-4: Reverse Left half pyramid
N = 6

for A in range(1, N + 1):
    for K in range(1, A):
        print(" ", end="")
        
    for K in range(1, N - A + 2):
        print("*", end="")
    print()

#Pattern-5: Square fill
for I in range(1, 11):
    for J in range(1,11):
        print("*", end="")
    print()
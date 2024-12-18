'''
Q57. Write a program to get input from users email and atleast 3 email should repeat and
5 unique email id using list?
'''
User_data = [ 'aryanshivgunde@gmail.com','aryanshivgunde@gmail.com','meghrajshivgunde@gmail.com','shwetashiivgunde@gmail.com','shwetashivgunde@gmail.com','athravshiivgunde@gmaill.com' ]

R = int( input( " Enter the range of the data: " ) )

for K in range(0,R):
    ELe = input( " Enter element: " )
    User_data.append(ELe)

print( " The data: ", User_data )


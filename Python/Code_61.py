#Write a program to accept p n and r and calculate it Simple interest
P = int( input( " Enter principal amount: "  ) )
R = int( input( " Enter rate of interest: " ) )
T = int( input( " Enter time period: " ) )

Si = ( P * R * T )/ 100

print( " \n Simple interest of  Rs ", P, "is", Si )
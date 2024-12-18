#Write a program to get radius of circle from user and print its area, circumstance and diameter

Pi = float( 3.14 )

R = int( input( " Enter radius: " ) )

A = Pi * R * R
Cir = int( 2 * Pi * R )
Dia = R * 2

print( " \n Area of circle = ", A )
print( " Circumference of circle = ", Cir )
print( " Diameter of circle = ", Dia )
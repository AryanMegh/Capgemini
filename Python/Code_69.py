#Write a program to print the code of cricket
#If a team scores 200 in 20 over
#Then how much does team 2 has to score in 1 over

N_of_score = 200
N_of_over = 20

T2_score = int( input( " Enter score: " ) )

T_score = N_of_score * T2_score / N_of_over

print( " Score = ", T_score )
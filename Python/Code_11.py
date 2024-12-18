'''
Q11. Write a program to accept score of 
two team and make a decision which team wom the match
'''

indiaScore = int( input( " Enter score of India team: " ) )
englandScore = int( input( " Enter score of England team: " ) )

if indiaScore > englandScore:
    print( " India won the match " )
else:
    print( " England won the match " )
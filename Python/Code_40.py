'''
Q40) Write a program to calculate simple interest?
'''

#Taking values from user to calcuate simple interest

Principal_amount = int( input( " Enter principal amount: " ) )
Rate_of_interest = int( input( " Enter rate of interest: " ) )
Time_period = int( input( " Enter time period till time you want to keep mony in the bank: " ) )

#A formula to calculate simple interest
Simple_interest = (Principal_amount * Rate_of_interest * Time_period)/100

#Printing the simple interest using print statement
print( " The simple interest of ", Principal_amount, "with rate of interest", Rate_of_interest, "with", Time_period, "period of time is:", Simple_interest, "%" )
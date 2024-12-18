'''
Q4) Write a program to accept basic salary from user 
and Give 10% of DA on basic salary ,12% HRA on basic salary to employee 
if the salary is 
more than 50000 calculate total salary?
'''

Emp_name = input( " Enter name: " )
Sal = int( input( " Enter your salary ($): " ) )
HRA = int( input( " Enter HRA ($): " ) )
DA = int( input( " Enter DA ($): " ) )


HRA = Sal * 0.18
DA = Sal * 0.10
PF = Sal * 0.12
Gross_salary = Sal + DA + HRA
Net_salary = Gross_salary - PF

print( " Employee name = ", Emp_name )
print( " Salary ($) = ", Sal )
print( " DA (30%): ", DA )
print( " HRA (18%): ", HRA)
print( " PF (12%): ", PF)
print( " Gross Salary: ", Gross_salary )
print( " Net Salary: ", Net_salary )
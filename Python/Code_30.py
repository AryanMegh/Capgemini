'''
Q30. Write a program to print the description of user.
'''

Name = input( " Enter your name: " )
Age = int( input( " Enter your age: " ) )

Formatted_str = f"My name is %s and I am %d years old." %( Name, Age )

print( Formatted_str )

print( " My name is ", Name, " and i am ", Age, " years old. " )
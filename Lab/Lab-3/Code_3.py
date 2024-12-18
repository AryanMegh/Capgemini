'''
Q3. Write a program to create dictionaries for below task and perform all the above operations on it.
Each product in a supermarket is associated with its price.
Each student in a school is associated with their grade.
Each customer ID in a company is associated with a customer name.
'''

Customer_dict = {
    1 : "Alice",
    2 : "Bob",
    3 : "Charlie",
    4 : "Diana",
    5 : "Eve"
}

print( " The data = ", Customer_dict )
print( " The data type of data is: ", type(Market_dict) )

New_data = Market_dict.copy()

print( " The copied data is: ", New_data )
print( " The total length of the dictonary is: ", len(Market_dict) )
print( " The keys in the dictonary is: ", Market_dict.keys() )
print( " The values in the dictonary is: ", Market_dict.values() )
print( " The data in the dictonary after clearing data is: ", Market_dict.clear() )

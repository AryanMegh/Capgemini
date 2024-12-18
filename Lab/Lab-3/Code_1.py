'''
Q1. Write a program to create dictionaries for below task and perform all
the above operations on it.
Each product in a supermarket is associated with its price.
Each student in a school is associated with their grade.
Each customer ID in a company is associated with a customer name.
'''

Market_dict = {
    "Apple" : 1.5,
    "Banana" : 0.5,
    "milk" : 2.5,
    "bread" : 1.8,
    "cheese" : 3.0
}

print( " Data = ", Market_dict )
print( " The data type of data is: ", type(Market_dict) )

New_data = Market_dict.copy()

print( " The copied data is: ", New_data )
print( " The total length of the dictonary is: ", len(Market_dict) )
print( " The keys in the dictonary is: ", Market_dict.keys() )
print( " The values in the dictonary is: ", Market_dict.values() )
print( " The data in the dictonary after clearing data is: ", Market_dict.clear() )

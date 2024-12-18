'''
Q2. Write a program to create dictionaries for below task and perform all the above operations on it.
Each product in a supermarket is associated with its price.
Each student in a school is associated with their grade.
Each customer ID in a company is associated with a customer name.
'''

Student_dict = {
    "Alice" : "A",
    "Bob" : "B",
    "Charlie" : "C",
    "Diana" : "A",
    "Eve" : "B"
}

print( " The data = ", Student_dict )
print( " The data type of data is: ", type(Student_dict) )

New_data = Student_dict.copy()

print( " The copied data is: ", New_data )
print( " The total length of the dictonary is: ", len(Student_dict) )
print( " The keys in the dictonary is: ", Student_dict.keys() )
print( " The values in the dictonary is: ", Student_dict.values() )
print( " The data in the dictonary after clearing data is: ", Student_dict.clear() )

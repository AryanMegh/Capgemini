class Employee:
    Name = "Aryan"
    Age = 20
    Designation = "Developer"
    
    def Info(self):
        print( "My name is", self.Name, "and i am ", self.Age, "years old, and i am an", self.Designation )
        
A = Employee()

A.Info()
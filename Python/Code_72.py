class Student:
	def __init__(self, N, Add,  C, S):
		self.N = Name
		self.Add  = Address
		self.S = State
		self.Count = C

	def Acceptdata(self):
		self.N = str( input( " Enter your name: " ) )
		self.Add = str( input( " Enter your address: " ) )
		self.S = str( input( " Enter your state: " ) )
		self.C = str( input( " Enter your country: " ) )

	def Dispdata(self):
		print( " Student data: " )
		print( " Name: ", N )
		print( " Country: ", C )
		print( " State: ", S )
		print( " Address: ", Add )

Stud_obj = new Student()

Stud_obj.Acceptdata()
Stud_obj.Dispdata()	
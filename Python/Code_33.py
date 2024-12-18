#Q33. Write a program to reverse a number

Num = int( input( " Enter number: " ) )

Temp = Num

Reverse = 0

while Temp > 0:
    Reminder = Temp % 10
    Reverse = (Reverse * 10) + Reminder
    Temp = Temp // 10
    
print( " The reverse of ", Num, "is:", Reverse )
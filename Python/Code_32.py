#Write a program to check if the entered number is a plindadrome number.

Num = int( input( " Enter number: " ) )

Temp = Num

Reverse = 0

while Temp > 0:
    Reminder = Temp % 10
    Reverse = (Reverse * 10) + Reminder
    Temp = Temp // 10

if Num == Reverse
    print( Num, " is palindrome number " ) 
else:
    print( Num, " is not palindrome number. " )
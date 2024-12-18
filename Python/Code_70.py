def Fibonacci_series(Limit):
    Fib_series = []
    A, B = 0, 1

    print( " Value of A: ", A )
    print( " Value of B: ", B )

    while A <= Limit:
        Fib_series.append(A)
        A, B = B, A + B
    
    return " Fibonacci series is: ", Fib_series

print( " Fibonacci series from 0 to 50 is: " )

Num = int( input( " Enter number: " ) )

Fib_series = Fibonacci_series(Num)

print(Fib_series)
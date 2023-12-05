def fibonacci(n):
    fib_series = [0, 1]  # Initialize the first two terms of the Fibonacci sequence

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_series

    for i in range(2, n):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)

    return fib_series

try:
    n = int(input("Enter the number of Fibonacci terms to calculate: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci(n)
        print("The first {} terms of the Fibonacci sequence:".format(n))
        print(result)
except ValueError:
    print("Invalid input. Please enter a positive integer.")

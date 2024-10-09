def first_fib():
    fib = [0, 1]
    for i in range(2, 5):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)

# CALL FOR OUTPUT
first_fib()
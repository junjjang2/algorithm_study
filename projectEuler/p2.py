even_sum = 0
fib_bef = 1
fib_curr = 2
while fib_curr < 4000000:
    if fib_curr % 2 == 0:
        even_sum += fib_curr
    fib_bef, fib_curr = fib_curr, fib_bef + fib_curr
print(even_sum)

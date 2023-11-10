num = 600851475143
i = 2
max_prime = i
while num > 1:   # calculate the largest prime factor of num
    if num % i == 0:
        num /= i
        max_prime = i
    else:
        i += 1
    
print(max_prime)

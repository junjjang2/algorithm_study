prime_cnt = 1
primes = [2]
i = 3
    
while prime_cnt < 10001:
    isprime = True
    for prime in primes:
        if i % prime == 0:
            isprime = False
            break
    if isprime:
        primes.append(i)
        prime_cnt += 1
    i += 1

print(primes[-1])

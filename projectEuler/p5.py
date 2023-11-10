#primes_lower_than_10 = [2, 3, 5, 7]
primes_lower_than_20 = [2, 3, 5, 7, 11, 13, 17, 19]

miminum_common_multiple = 1

for prime in primes_lower_than_20:
    max_power = prime
    while max_power*prime < 20:
        max_power *= prime
    miminum_common_multiple *= max_power

print(miminum_common_multiple)

# from p7.py

"""
prime_cnt = 1
primes = [2]
i = 3
while i < 2000000:
    isprime = True
    for prime in primes:
        if i % prime == 0:
            isprime = False
            break
    if isprime:
        primes.append(i)
        prime_cnt += 1
    i += 1

print(sum(primes))
"""

# 에라토스테네스의 체
max_n = 2000000
nums = [True for i in range(max_n)]
primes = []

for i in range(2, max_n):
    if nums[i]:
        primes.append(i)
        for j in range(i, max_n, i):
            nums[j] = False
            
print(sum(primes))

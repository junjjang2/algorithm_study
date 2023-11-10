import math

def num_divisors(n):
    count = 0
    root = int(math.sqrt(n))
    if root*root == n:
        count += 1
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            count += 2
    return count

triangle_number = 0
idx = 1
while True:
    triangle_number += idx
    if num_divisors(triangle_number) > 500:
        print(triangle_number)
        # >>>76576500
        break
    
    idx += 1 


import math
import itertools
from cProfile import Profile
from pstats import SortKey, Stats


def calcPrime(n):
    # from p10.py
    pArray = [True] * n
    pArray[0] = False
    pArray[1] = False  
    for i in range(2, n):
        if pArray[i]:
            for j in range(i+i, n, i):
                pArray[j] = False             
    return pArray

def get_combination(dim):
    arr = range(dim)
    result = None
    for i in range(1, len(arr)):
        if result is None:
            result = list(itertools.combinations(arr,i)) 
        else:
            result.extend(list(itertools.combinations(arr,i)) )

    for comb in result:
        yield comb
        
# Fastest... impressive
def replace_digit(n, digits, replacement):
    n_list = list(str(n))
    for digit in digits:
        n_list[digit] = replacement
    return int("".join(n_list)) # "join" is faster than "+
    
    
def solution(family_size=7):
    ed = 9
    
    dim = 2
    while True:
        isPrime = calcPrime(n=10**dim)
        
        st = 10**(dim-1)
        ed += st * 9
        for org in range(st, ed):
            for comb in get_combination(dim):
                i = org
                cnt = 0
                first_prime = None
                # calc family
                for n in range(1 if 0 in comb else 0, 10):
                    
                    i = replace_digit(i, comb, n)
                    if isPrime[i]:
                        if cnt == 0:
                            first_prime = i
                        cnt += 1
                if cnt == family_size:
                    print(first_prime)
                    return
        dim += 1

#print(replace_digit(12345, 0, 9))
#solution()


with Profile() as profile:
    print(f"{solution(family_size=8)}")
    (
        Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.CALLS)
        .print_stats()
    )
    
    """
    121313
         106026045 function calls in 265.401 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
101695108  121.995    0.000  121.995    0.000 p51.py:30(replace_digit)
  4210631    7.982    0.000    8.000    0.000 p51.py:18(get_combination)
   120291    0.017    0.000    0.017    0.000 {built-in method builtins.len}
        5    0.444    0.089    0.444    0.089 p51.py:7(calcPrime)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1  134.961  134.961  265.400  265.400 p51.py:41(solution)
        1    0.000    0.000    0.000    0.000 cProfile.py:51(create_stats)
        1    0.000    0.000    0.000    0.000 pstats.py:107(__init__)
        1    0.000    0.000    0.000    0.000 pstats.py:117(init)
        1    0.000    0.000    0.000    0.000 pstats.py:136(load_stats)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}   
    """

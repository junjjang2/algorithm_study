def sum_of_square(n: int):
    if n <= 1:
        return n
    result = 0
    for i in range(1, n+1):
        result += i**2 
    return result

def square_of_sum(n : int):
    if n <= 1:
        return n
    
    return (n*(n+1)//2)**2

print(square_of_sum(100) - sum_of_square(100))
# >>>25164150

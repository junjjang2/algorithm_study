def isPalindrom(num):
    if num < 100001:
        return False
    for i in range(5, 0, -2):
        if num % 10 == num // 10**i:
            num = num % 10**i // 10
        else:
            return False
    return True

print(isPalindrom(900009))

a = 999
b = 999
max_palindrom= 100001
while True:
    if a * b < max_palindrom:
        if a == b:
            break
        b -= 1
        a = b
    else:
        if isPalindrom(a * b):
            max_palindrom = a * b
            b -= 1
            a = b
        else:
            a -= 1

print(max_palindrom)

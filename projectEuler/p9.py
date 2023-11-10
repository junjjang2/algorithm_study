

a = 1
b = 2
while True:
    c = 1000 - b - a
    if b < c:
        if a**2 + b**2 == c**2:
            print(a*b*c)
            break
        else:
            b += 1
    else:
        a += 1
        b = a + 1        

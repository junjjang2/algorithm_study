# Power Digit Sum

def solution(n):
    return sum(map(int, str(2<<(n-1))))

print(solution(1000))
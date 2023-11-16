# lattice paths

#n x m grid일 때, 오른쪽으로 n번, 아래로 m번 움직이는 경우의 수는
#n개의 동일한 오른쪽 이동과, m개의 아래 이동을 나열하는 경우의 수와 같다.
#따라서 (n+m)! / n!m! 이다.

def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def solution(n, m):
    return fact(n+m) / fact(n) / fact(m)

n = 20
m = 20

print(int(solution(n, m)))
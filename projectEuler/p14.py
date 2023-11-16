# Longest Collatz Sequence


def collatz(n):
    if n % 2 == 0: # if n is even
        return n>>1
    else: #if n is odd
        return 3*n + 1

def solution(nn=1000000):
    dynamic_dict = dict() # some bigger number
    dynamic_dict[1] = 1
    m_cnt = 0 
    for n in range(2, nn): # under one million
        if n in dynamic_dict:
            continue
        cnt = 1
        queue_chain = [n]
        org = n
        while n > 1:
            n = collatz(n)
            if n in dynamic_dict:
                cnt = dynamic_dict[n] + cnt
                break
            queue_chain.append(n)
            cnt += 1
        for i in range(len(queue_chain)):
            dynamic_dict[queue_chain[i]] = cnt - i
        if m_cnt < cnt:
            start_num = org
            m_cnt = cnt
    return start_num

print(solution(1000000))

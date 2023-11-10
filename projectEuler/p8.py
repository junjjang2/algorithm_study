import time


thousand_number = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", "").strip()
def solution1():
    global thousand_number
    start = time.time()
    num_array = [int(i) for i in thousand_number]

    n_adjacent = 13

    #max_product = 0
    prev_product = 0

    st = 0
    ed = 0   
    while ed < st + n_adjacent and ed < 1000:
        if num_array[ed] == 0:
            st = ed + 1
            ed = st
            prev_product = 0
        else:
            if prev_product == 0 :
                prev_product = num_array[ed]
            else:
                prev_product *= num_array[ed]
            ed += 1
            
    max_product = prev_product
        
    while ed < 1000:
        if num_array[ed] == 0:
            st = ed + 1
            ed = st
            prev_product = 0

            while ed < st + n_adjacent and ed < 1000:
                if num_array[ed] == 0:
                    st = ed + 1
                    ed = st
                    prev_product = 0
                else:
                    if prev_product == 0 :
                        prev_product = num_array[ed]
                    else:
                        prev_product *= num_array[ed]
                    ed += 1
        else:
            prev_product = prev_product // num_array[st] * num_array[ed]
            st += 1
            ed += 1
        
        if prev_product > max_product:
            max_product = prev_product
        
        
    
    end = time.time()
    print(max_product)

    # time:  0.0009968280792236328 s
    print("time: ",end - start)
    

def solution2():
    global thousand_number
    start1 = time.time()

    non_zero_series = (series for series in thousand_number.split("0") if len(series) >= 13)
    max_product = 0
    n_adjacent = 13
    for series in non_zero_series:
        series = list(map(int, series))
        
        prev_product = 1
        for i in series[:n_adjacent]:
            prev_product *= i
        if prev_product > max_product:
                max_product = prev_product
        
        st = 0
        ed = n_adjacent
        while ed < len(series):
            prev_product = prev_product // series[st] * series[ed]
            if prev_product > max_product:
                max_product = prev_product
            st += 1
            ed += 1
    
    end1 = time.time()

    print(max_product)
    

    print("time: ",end1 - start1)

solution2()

solution1()

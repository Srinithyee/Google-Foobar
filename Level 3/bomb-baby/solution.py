def solution(F, M):
    f, m = long(F), long(M)
    result = 0
    while not (f == 1 and m == 1):
        if f <= 0 or m <= 0:
            return "impossible"
        if f == 1:
            return str(result + m - 1)
        else:
            result += long(m/f)
            f, m = m % f, f 
    return str(result)
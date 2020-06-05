def solution(total_lambs):
    
    if total_lambs >= 10**9:
        return 0
    twice = []
    i = 0
    runningtotal = 0
    while i <= total_lambs:
        current = 2**i
        twice.append(current)
        runningtotal = runningtotal + current
        if runningtotal > total_lambs:
            break
        i = i+1
    fibo = [1,1]
    fibototal = 2
    j = 2
    while j <= total_lambs:
        value = fibo[j-1] + fibo[j-2]
        fibo.append(value)
        fibototal = fibototal + int(fibo[j])
        if fibototal > total_lambs:
            break
        j = j+1
    result = len(fibo) - len(twice)
    return abs(result)
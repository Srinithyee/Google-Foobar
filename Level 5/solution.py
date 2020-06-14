from collections import Counter

def factorial(number):
    prime = [True]*(number + 1)
    result = 1
    for i in xrange (2, number+1):
        if prime[i]:
            j = i+i
            while j <= number:
                prime[j] = False
                j += i
            sum = 0
            t = i
            while t <= number:
                sum += number/t
                t *= i
            result *= i**sum
    return result

def gcd(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 

def counter(c, n):
    count_cycle=factorial(n)
    for a, b in Counter(c).items():
        count_cycle//=(a**b)*factorial(b)
    return count_cycle        

def segmenter(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in segmenter(n-i, i):
            yield [i] + p

def solution(w, h, s):    
    grid=0
    for width in segmenter(w):
        for height in segmenter(h):            
            moves=counter(width, w)*counter(height, h)
            grid+=moves*(s**sum([sum([gcd(i, j) for i in width]) for j in height]))

    return str(grid//(factorial(w)*factorial(h)))


# 1
def tribonacci(n):
    if n==0 or n==1 or n==2:
        return 1
    return trib2(n-1, 1, 1, 1)

def trib2(a,x,y,z):
    if a == 0:
        return y
    return trib2(a-1, y, z, x+y+z)

# 2
def histograma(n):
    
    if n == []:
        return ""
    
    [int(x) for x in n if x != 0]
    print(n[0] * "*")
    novo = n[1:]
    return histograma(novo)

# 3
import math
def kp(n):
    lul = [int(i) for i in range(2,n+1)]
    lulMasFact = [math.factorial(i) for i in lul]
    return div(n,lul,lulMasFact,1)

def div(n,i,iF,v):
    if iF[v] % n == 0:
        return i[v]
    return div(n,i,iF,v+1)

# 4
def nat(n):
    if n == 0:
        return []
    return nat(n-1) + [nat(n-1)]

# 5
def seqPd(n):
    if n==0 or n==1 or n==2:
        return 1
    if n==3 or n==4:
        return 2
    return seqPd2(n-1,1,1,1)
    
def seqPd2(x,a,b,c):
    if x == 0:
        return b
    return seqPd2(x-1, b, c, a+b)
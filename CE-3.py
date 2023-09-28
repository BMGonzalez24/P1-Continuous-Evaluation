# 1
def noIntervalo(n,a,b):
    return n >= a and n <= b

# 2
def eRetangulo(a, b, c, d):
  return a == b and c == d or a == c and b == d or a == d and b == c

# 3
def somaKPotencias(k, xs):
    if len(xs)==0 or k==0:
        return 0
    else:
        return k*xs[0]**k + somaKPotencias(k, xs[1:])
# 4
def ePangrama(str): 
    abc = "abcdefghijklmnopqrstuvwxyz"
    for char in abc: 
        if char not in str.lower(): 
            return False
    return True

# 5
def linhaPascal(x):
        y =[]
        y.append(1)
        for i in range(1, len(x)):
            sum = x[i-1] + x[i]
            y.append(sum)
        y.append(1)
        return y
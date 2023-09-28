# 1
def ordenarTriplo(a,b,c):

    a = int(a)
    b = int(b)
    c = int(c)

    d = (a,b,c)

    d = tuple(sorted(d,reverse = True))

    return d

# 2
def mediana(valores):

    valores =  [int(i) for i in valores]
    valores.sort()

    if len(valores) % 2 == 0:
        meio = int((len(valores) / 2))
        return (valores[meio-1] + valores[meio]) / 2

    if len(valores) % 2 != 0:
        meio = int((len(valores)+1) / 2)
        return float(valores[meio-1])

# 3
def numDigitos(n):
  
 if n < 10:
  return 1

 else:
  a = n /10
  return 1 + numDigitos(a)
 
# 4
def minimo(n):

    if len(n) != 1:
        if n[0] > n[1]:
            n.remove(n[0])
            return(minimo(n))
        
        if n[1] > n[0]:
            n.remove(n[1])
            return(minimo(n))

    if len(n) == 1:
        return n[0]

# 5
def apenas_5_3(n):

    n = int(n)

    if n >= 0:
        if n % 3 == 0 and n > 3:
            return apenas_5_3(n//3) or apenas_5_3(n-5)
        elif n > 5:
            return apenas_5_3(n-5)
        return n == 3 or n == 5

    else:
        return False
# 1
def contarDigitos(n):
  ## TODO
    x = 1
    if n < 0:
        return contarDigitos(n*(-1))
    while n > 1:
        n //= 10
        x += 1
    return x

# 2
def idxMaxPar(lista):
  ## TODO
    pares = []
    for i in lista:
        pares = [i for i in lista if i%2==0]
    if pares == []:
        return -1
    x = max(pares)
    paresFinal = [i for i, y in enumerate(lista) if x==y]
    final = int(paresFinal[0])
    return final

# 3
def neutralizarSinais(s1, s2):
    ## TODO
    final = ""
    s3 = list(zip(s1,s2))
    for x in s3:
        if x == ('+', '+'):
            final = final + "+"
        if x == ('-', '-'):
            final = final + "-"
        if x == ('+', '-') or x == ('-', '+'):
            final = final + "0"
    return final

# 4
def somaAcc(lista):
  ## TODO
    final = []
    n = len(lista)
    x = 1
    
    if lista == []:
        return []
    
    final.append(lista[0])
    final.append(lista[0]+lista[1])
    
    while x+1 < n:
        final.append(final[x]+lista[x+1])
        x = x+1
        
    return final

# 5
def classificar(paisagem):
    ## TODO
    for i in range(len(paisagem)):
        if paisagem[i] < paisagem[i+1] and paisagem[-1] < paisagem[-2]:
            return "montanha"
        if paisagem[i] > paisagem[i+1] and paisagem[-1] > paisagem[-2]:
            return "vale"
        else:
            return "nenhum"
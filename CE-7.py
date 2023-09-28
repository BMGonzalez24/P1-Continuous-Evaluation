# 1
def pivotSoma(lista):
    ## TODO
    for i,x in enumerate(lista):
        ini=lista[:i]
        somaIni=sum(ini)
        
        fim=lista[i+1:]
        somaFim=sum(fim)
        
        if somaIni == somaFim:
            return i
        
    if somaIni != somaFim or lista == []:
        return -1

# 2
s = "50515253"  # exemplo de string

def contarAscendente(s):
    ## TODO
    s = [x for x in str(s)]
    novaLista = [int(s[0]+s[1])]
    total = len(s)
    rep = 0
    rep2 = 2
    if total < 4:
        return False
    while rep2 < total and novaLista[rep] < int(s[rep2]+s[rep2+1]):
        novaLista.append(int(s[rep2]+s[rep2+1]))
        rep += 1
        rep2 += 2
    if sorted(novaLista) == novaLista:
        return True
    return False
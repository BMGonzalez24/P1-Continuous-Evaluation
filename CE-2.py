# 1
lista = [3**x for x in range(7, 19)]

# 2
numeros = [-2, 20, -16, 40, 34, -93, 34, -80, 72, -97, 5, -94, 97, 15, -28, -47, 12, -17, -20, -13, -54, 95, -8, 89, 38, -45, -54, -71, -2, -41, 92, 23, -71, -96, -79, 81, 6, -91, -86, -56, 4, -37, 91, -97, -65, -39, -68, -54, 25, 41, 57, -90, -18, 4, -42, 44, -59, 33, -17, 65, -54, -22, 74, -78, 81, -58, 60, 75, -94, 26, -49, 95, 31, -70, 27, 80, -86, 2, 4, -4, 32, -41, -63, -98, 32, 29, -100, 48, -45, 56, -76, 50, 81, -29, -8, 2, -96, 45, 74, -91]

positivos = list(filter(lambda x: x >= 0, numeros))

# 3
palavras = "ABLE ACEITA ACEITAÇÃO ACEITÁVEL ACEITO ACEITANDO AÇÃO ATIVAR ACTIVE ADD ADIÇÃO ADORÁVEL VANTAGEM AFIRME SEM IDADE CONCORDA AGRADÁVEL AID AIM ABUNDÂNCIA PRESTAÇÃO DE CONTAS REALIZAÇÃO REALIZAR EXACTIDÃO FAÇANHA ALCANÇAR AGRADECIMENTO ADAPTABILIDADE ADVENTURE ADVENTUROUS AGILIDADE AGILIDADE AMBIÇÃO ANTECIPAÇÃO AGRADECEMOS APPRECIATION GRATA APPRECIATIVENESS ASSERTIVIDADE ASSERTIVA ATENÇÃO AUDÁCIA AWARE CONSCIÊNCIA AUTÊNTICO AUTENTICIDADE ABRACADABRA ATRAÇÃO PERMITEM PERMITINDO CARINHO CARINHOSO ABSORVIDO ALERT SURPREENDIDO AWE AWED ANIMATE ANIMADO ANIMANDO ANIMAÇÃO ANIMATENESS ARDENTE SURPRESA IMPRESSIONANTE AWESOMENESS EXCITADO SURPREENDIDO ASTONISHING DIVERTIDO AIR AIRNESS ALOHA ADORE ADMIRE ADMIRÁVEL ALLURE ANGEL ANGÉLICO O ALTRUÍSMO ALTRUÍSTAS ABUNDAM ABUNDANTE ABOUNDS ABUNDANTE ABSOLUTO ABSOLUTAMENTE ACESSÍVEL ACLAMADO ACOMODAR ACOMODADO ACOMODAÇÃO ACOMODANDO AMPLA APRECIATIVO ALEGRIA AMIN ACCENTUACTIVITY"
palavrasSplit = palavras.split(" ")
pequenas = list(filter(lambda x: len(x) <= 5, palavrasSplit))

# 4
listaA = [x for x in range(0, 201)]
listaPares = list(())

for y in listaA:
    for x in range(-100, y+1):
        if ((x**2 + x) == 3*y) and (x % 3 == 0 or x % 5 == 0):
            listaPares.append((x,y))
massa = float(input('massa: '))
altura = float(input('altura: '))

def imc(massa, altura):
    i = massa / (altura**2)
    return i

indice = imc(massa, altura)

def resultado(indice):
    if indice < 18.5:
        c = 'muito abaixo do peso'
    elif indice < 25:
        c = 'peso adequado'
    elif indice < 30:
        c = 'sobrepeso'
    else: 
        print('obeso')
    
    r = f'seu imc é {indice} e pode ser classificado como {c}'
    print(r)

resultado(indice)
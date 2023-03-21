import matplotlib

import numpy as np


# recebe do usuario as entradas da função
def _input () :
    global a, b, c 
    a = int(input("insita um valor para ax²:"))
    b = int(input("insita um valor para bx:"))
    c = int(input("insita um valor para c²:"))

    return a, b, c
_input()



def calc_delta (a, b, c): 
    delta = b*b - 4*a*c
    print(delta)
    return delta
delta = calc_delta(a, b, c)


def calc_raizes (a, b, delta): 
    if delta < 0 :
        resultado = "a equação não possui raizes nos números reais, somente nos complexos"
    elif delta == 0 :
        x = -b / 2*a 
        resultado = f'a equação possui apenas uma raiz real, ja que delta é 0, sua raiz é: {x}'
    else :
        x1 =  (-b - np.sqrt(delta)) / (2*a)
        x2 =  (-b + np.sqrt(delta)) / (2*a)
        resultado = f'a equação possui duas raizes reais, já que seu delta é maior que 0, suas raizes são: {x1} e {x2}'
    return print(resultado)
calc_raizes(a, b, delta)